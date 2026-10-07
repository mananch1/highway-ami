import React, { useState, useEffect, useRef, useContext } from 'react';
import SockJS from 'sockjs-client';
import { Client } from '@stomp/stompjs';
import { getChatMessages } from '../api/api';
import { AuthContext } from '../context/AuthContext';

const Chat = ({ incidentId, guestToken, guestName }) => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const stompClientRef = useRef(null);
  const messagesEndRef = useRef(null);
  const { user } = useContext(AuthContext);

  useEffect(() => {
    // Load history
    const loadHistory = async () => {
      try {
        const history = await getChatMessages(incidentId);
        setMessages(history || []);
      } catch (err) {
        console.error('Failed to load chat history', err);
      }
    };
    loadHistory();

    // Setup STOMP
    const socketUrl = guestToken ? `/ws?token=${guestToken}` : '/ws'; // Ensure proper backend config if needed, otherwise fallback to basic
    const client = new Client({
      webSocketFactory: () => new SockJS('/ws'),
      connectHeaders: guestToken ? { Authorization: `Bearer ${guestToken}` } : (user ? { Authorization: `Bearer ${localStorage.getItem('token')}` } : {}),
      debug: (str) => {
        // console.log(str);
      },
      onConnect: () => {
        client.subscribe(`/topic/chat/${incidentId}`, (message) => {
          if (message.body) {
            const newMsg = JSON.parse(message.body);
            setMessages((prev) => [...prev, newMsg]);
          }
        });
      },
      onStompError: (frame) => {
        console.error('Broker reported error: ' + frame.headers['message']);
        console.error('Additional details: ' + frame.body);
      }
    });

    client.activate();
    stompClientRef.current = client;

    return () => {
      if (client.active) {
        client.deactivate();
      }
    };
  }, [incidentId, guestToken, user]);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const handleSend = (e) => {
    e.preventDefault();
    if (!input.trim() || !stompClientRef.current?.active) return;

    const currentSenderName = user?.name || guestName || 'Guest';
    const messageObj = {
      incidentId: incidentId,
      message: input,
      senderName: currentSenderName
    };

    stompClientRef.current.publish({
      destination: `/app/chat/${incidentId}`,
      body: JSON.stringify(messageObj)
    });

    setInput('');
  };

  const myName = (user?.name || guestName || 'Guest').trim().toLowerCase();

  return (
    <div className="card" style={{ display: 'flex', flexDirection: 'column', height: '400px', padding: '1rem' }}>
      <h3 style={{ marginBottom: '1rem', borderBottom: '1px solid var(--border)', paddingBottom: '0.5rem' }}>Chat</h3>
      
      <div style={{ flex: 1, overflowY: 'auto', marginBottom: '1rem', display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
        {messages.map((msg, index) => {
          const msgSender = (msg.senderName || '').trim().toLowerCase();
          const isMe = msgSender === myName;
          return (
            <div key={index} style={{
              alignSelf: isMe ? 'flex-end' : 'flex-start',
              backgroundColor: isMe ? 'var(--primary)' : '#f1f5f9',
              color: isMe ? 'white' : 'var(--text-main)',
              padding: '0.5rem 1rem',
              borderRadius: '8px',
              maxWidth: '80%'
            }}>
              <div style={{ fontSize: '0.75rem', marginBottom: '0.25rem', opacity: 0.8 }}>
                {msg.senderName} • {new Date(msg.timestamp || Date.now()).toLocaleTimeString()}
              </div>
              <div>{msg.message || msg.content}</div>
            </div>
          );
        })}
        <div ref={messagesEndRef} />
      </div>

      <form onSubmit={handleSend} style={{ display: 'flex', gap: '0.5rem', marginTop: 'auto' }}>
        <input 
          type="text" 
          value={input} 
          onChange={(e) => setInput(e.target.value)} 
          placeholder="Type a message..."
          style={{ margin: 0, flex: 1 }}
        />
        <button type="submit" className="primary">Send</button>
      </form>
    </div>
  );
};

export default Chat;
