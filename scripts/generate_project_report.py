#!/usr/bin/env python3
"""
Automated Academic Project Report Generator for DevOps Engineering
Generates:
1. docs/DEVOPS-PROJECT-REPORT-MANAN-CHAHAL-23102C0044.docx (Formatted Word Document)
2. docs/CONSOLIDATED-PROJECT-REPORT-MANAN-CHAHAL.md (Comprehensive Markdown Document)

Candidate: Manan Chahal (Roll No: 23102C0044)
Institution: Vidyalankar Institute of Technology
Department: Computer Engineering
Course: DevOps Engineering Lab & Integrated Project (CSL702 / CSP702)
Academic Year: 2026-2027 (Semester VII - Div C)
"""

import os
import sys
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

DOCX_OUTPUT_PATH = os.path.join("docs", "DEVOPS-PROJECT-REPORT-MANAN-CHAHAL-23102C0044.docx")
MD_OUTPUT_PATH = os.path.join("docs", "CONSOLIDATED-PROJECT-REPORT-MANAN-CHAHAL.md")
SCREENSHOT_PATH = os.path.join("target", "screenshots", "Journey1_GuestEmergency_20261029_110652_880.png")

# Palette
COLOR_NAVY = RGBColor(15, 23, 42)       # #0f172a - Primary Header / Title
COLOR_BLUE = RGBColor(29, 78, 216)      # #1d4ed8 - Accent / Subheadings
COLOR_SLATE = RGBColor(51, 65, 85)      # #334155 - Subtitle / Heading 3
COLOR_BODY = RGBColor(30, 41, 59)       # #1e293b - Main body text
COLOR_MUTED = RGBColor(100, 116, 139)   # #64748b - Muted captions / footers
COLOR_GREEN = RGBColor(21, 128, 61)     # #15803d - Success / verified tags

HEX_NAVY = "0F172A"
HEX_LIGHT_BLUE = "EFF6FF"
HEX_LIGHT_GRAY = "F8FAFC"
HEX_BORDER = "CBD5E1"
HEX_ACCENT_BAR = "1D4ED8"

def set_cell_background(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    tcPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>'))

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(
        f'<w:tcMar {nsdecls("w")}>'
        f'<w:top w:w="{top}" w:type="dxa"/>'
        f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
        f'<w:left w:w="{left}" w:type="dxa"/>'
        f'<w:right w:w="{right}" w:type="dxa"/>'
        f'</w:tcMar>'
    )
    tcPr.append(tcMar)

def set_table_borders(table, hex_color=HEX_BORDER):
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'<w:top w:val="single" w:sz="6" w:space="0" w:color="{HEX_NAVY}"/>'
        f'<w:bottom w:val="single" w:sz="6" w:space="0" w:color="{HEX_NAVY}"/>'
        f'<w:left w:val="none"/>'
        f'<w:right w:val="none"/>'
        f'<w:insideH w:val="single" w:sz="4" w:space="0" w:color="{hex_color}"/>'
        f'<w:insideV w:val="none"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

def format_row(row, is_header=False, is_alt=False, widths=None):
    for i, cell in enumerate(row.cells):
        if widths and i < len(widths):
            cell.width = widths[i]
        if is_header:
            set_cell_background(cell, HEX_NAVY)
            set_cell_margins(cell, top=120, bottom=120, left=140, right=140)
            for p in cell.paragraphs:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                for run in p.runs:
                    run.font.bold = True
                    run.font.color.rgb = RGBColor(255, 255, 255)
                    run.font.size = Pt(9.0)
                    run.font.name = "Calibri"
        else:
            bg = HEX_LIGHT_GRAY if is_alt else "FFFFFF"
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=90, bottom=90, left=140, right=140)
            for p in cell.paragraphs:
                for run in p.runs:
                    run.font.size = Pt(9.0)
                    run.font.color.rgb = COLOR_BODY
                    run.font.name = "Calibri"

def add_callout_box(doc, text, title=None):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    table.columns[0].width = Inches(6.5)
    
    cell = table.cell(0, 0)
    set_cell_background(cell, HEX_LIGHT_BLUE)
    set_cell_margins(cell, top=130, bottom=130, left=180, right=160)
    
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'<w:top w:val="none"/>'
        f'<w:left w:val="single" w:sz="24" w:space="0" w:color="{HEX_ACCENT_BAR}"/>'
        f'<w:bottom w:val="none"/>'
        f'<w:right w:val="none"/>'
        f'</w:tcBorders>'
    )
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.15
    
    if title:
        r_title = p.add_run(f"{title}\n")
        r_title.bold = True
        r_title.font.name = "Calibri"
        r_title.font.size = Pt(10.0)
        r_title.font.color.rgb = COLOR_BLUE
        
    r_body = p.add_run(text)
    r_body.italic = True
    r_body.font.name = "Calibri"
    r_body.font.size = Pt(9.5)
    r_body.font.color.rgb = COLOR_BODY
    
    p_spacer = doc.add_paragraph()
    p_spacer.paragraph_format.space_before = Pt(0)
    p_spacer.paragraph_format.space_after = Pt(3)

def add_code_block(doc, code_str, caption=None):
    if caption:
        p_cap = doc.add_paragraph()
        p_cap.paragraph_format.space_before = Pt(6)
        p_cap.paragraph_format.space_after = Pt(2)
        r_cap = p_cap.add_run(f"Listing: {caption}")
        r_cap.font.name = "Calibri"
        r_cap.font.size = Pt(9.0)
        r_cap.font.bold = True
        r_cap.font.color.rgb = COLOR_SLATE

    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    table.columns[0].width = Inches(6.5)
    
    cell = table.cell(0, 0)
    set_cell_background(cell, HEX_LIGHT_GRAY)
    set_cell_margins(cell, top=100, bottom=100, left=150, right=150)
    
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'<w:top w:val="single" w:sz="4" w:space="0" w:color="{HEX_BORDER}"/>'
        f'<w:left w:val="single" w:sz="4" w:space="0" w:color="{HEX_BORDER}"/>'
        f'<w:bottom w:val="single" w:sz="4" w:space="0" w:color="{HEX_BORDER}"/>'
        f'<w:right w:val="single" w:sz="4" w:space="0" w:color="{HEX_BORDER}"/>'
        f'</w:tcBorders>'
    )
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.05
    
    r = p.add_run(code_str)
    r.font.name = "Consolas"
    r.font.size = Pt(8.0)
    r.font.color.rgb = COLOR_NAVY
    
    p_spacer = doc.add_paragraph()
    p_spacer.paragraph_format.space_before = Pt(0)
    p_spacer.paragraph_format.space_after = Pt(3)

def add_heading_1(doc, text):
    h = doc.add_paragraph()
    h.paragraph_format.space_before = Pt(16)
    h.paragraph_format.space_after = Pt(5)
    h.paragraph_format.keep_with_next = True
    r = h.add_run(text)
    r.font.name = "Calibri"
    r.font.size = Pt(15)
    r.font.bold = True
    r.font.color.rgb = COLOR_NAVY
    return h

def add_heading_2(doc, text):
    h = doc.add_paragraph()
    h.paragraph_format.space_before = Pt(11)
    h.paragraph_format.space_after = Pt(3)
    h.paragraph_format.keep_with_next = True
    r = h.add_run(text)
    r.font.name = "Calibri"
    r.font.size = Pt(12.5)
    r.font.bold = True
    r.font.color.rgb = COLOR_BLUE
    return h

def add_heading_3(doc, text):
    h = doc.add_paragraph()
    h.paragraph_format.space_before = Pt(8)
    h.paragraph_format.space_after = Pt(2)
    h.paragraph_format.keep_with_next = True
    r = h.add_run(text)
    r.font.name = "Calibri"
    r.font.size = Pt(11)
    r.font.bold = True
    r.font.color.rgb = COLOR_SLATE
    return h

def add_body_p(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.15
    r = p.add_run(text)
    r.font.name = "Calibri"
    r.font.size = Pt(10)
    r.font.color.rgb = COLOR_BODY
    return p

def add_bullet_p(doc, text, bold_prefix=None):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(2.5)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = "Calibri"
        r_pre.font.size = Pt(10)
        r_pre.font.bold = True
        r_pre.font.color.rgb = COLOR_NAVY
    r = p.add_run(text)
    r.font.name = "Calibri"
    r.font.size = Pt(10)
    r.font.color.rgb = COLOR_BODY
    return p

def build_report():
    print("Initializing document...")
    doc = docx.Document()
    
    # Page Setup
    for s in doc.sections:
        s.top_margin = Inches(1.0)
        s.bottom_margin = Inches(1.0)
        s.left_margin = Inches(1.0)
        s.right_margin = Inches(1.0)
        s.different_first_page_header_footer = True
        
        # Header
        hp = s.header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hrun = hp.add_run("DevOps Integrated Project Report | Manan Chahal (23102C0044)")
        hrun.font.name = "Calibri"
        hrun.font.size = Pt(8.5)
        hrun.font.color.rgb = COLOR_MUTED
        
        # Footer
        fp = s.footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.LEFT
        frun = fp.add_run("Vidyalankar Institute of Technology — Department of Computer Engineering | BE CMPN-C")
        frun.font.name = "Calibri"
        frun.font.size = Pt(8.5)
        frun.font.color.rgb = COLOR_MUTED

    # ==========================================
    # COVER / TITLE PAGE
    # ==========================================
    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_inst.paragraph_format.space_before = Pt(10)
    p_inst.paragraph_format.space_after = Pt(4)
    r = p_inst.add_run("VIDYALANKAR INSTITUTE OF TECHNOLOGY\n")
    r.bold = True
    r.font.name = "Calibri"
    r.font.size = Pt(15)
    r.font.color.rgb = COLOR_NAVY
    
    r_sub = p_inst.add_run("DEPARTMENT OF COMPUTER ENGINEERING\nAffiliated to University of Mumbai | Accredited NAAC A+\nWadala (E), Mumbai - 400037\nAcademic Year 2026–2027")
    r_sub.font.name = "Calibri"
    r_sub.font.size = Pt(10)
    r_sub.font.color.rgb = COLOR_MUTED
    
    p_line = doc.add_paragraph()
    p_line.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_line.paragraph_format.space_before = Pt(14)
    p_line.paragraph_format.space_after = Pt(14)
    r_line = p_line.add_run("____________________________________________________________")
    r_line.font.color.rgb = RGBColor(203, 213, 225)
    
    p_rep_lbl = doc.add_paragraph()
    p_rep_lbl.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_rep_lbl.paragraph_format.space_before = Pt(10)
    p_rep_lbl.paragraph_format.space_after = Pt(8)
    r_rep = p_rep_lbl.add_run("A CONSOLIDATED DEVOPS PROJECT REPORT ON")
    r_rep.bold = True
    r_rep.font.name = "Calibri"
    r_rep.font.size = Pt(12)
    r_rep.font.color.rgb = COLOR_BLUE
    
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(6)
    p_title.paragraph_format.space_after = Pt(12)
    r_title = p_title.add_run("Automated DevOps CI/CD Pipeline & Highway Emergency Dispatch Platform")
    r_title.bold = True
    r_title.font.name = "Calibri"
    r_title.font.size = Pt(21)
    r_title.font.color.rgb = COLOR_NAVY
    
    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_before = Pt(0)
    p_sub.paragraph_format.space_after = Pt(24)
    r_sub = p_sub.add_run("Continuous Integration, Automated Quality Gating with Headless Selenium, Dockerized Multi-Tier Stacks, and Idempotent Ansible Cloud Deployment on AWS")
    r_sub.italic = True
    r_sub.font.name = "Calibri"
    r_sub.font.size = Pt(11)
    r_sub.font.color.rgb = COLOR_SLATE
    
    p_cand = doc.add_paragraph()
    p_cand.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cand.paragraph_format.space_before = Pt(16)
    p_cand.paragraph_format.space_after = Pt(4)
    r_by = p_cand.add_run("Submitted by:\n")
    r_by.font.name = "Calibri"
    r_by.font.size = Pt(10.5)
    r_by.font.color.rgb = COLOR_MUTED
    
    r_name = p_cand.add_run("MANAN CHAHAL\n")
    r_name.bold = True
    r_name.font.name = "Calibri"
    r_name.font.size = Pt(14)
    r_name.font.color.rgb = COLOR_NAVY
    
    r_meta = p_cand.add_run("Roll No: 23102C0044  |  Division: BE VII - Div C\nCourse: DevOps Engineering Lab & Integrated Project (CSL702 / CSP702)")
    r_meta.font.name = "Calibri"
    r_meta.font.size = Pt(10.5)
    r_meta.font.color.rgb = COLOR_SLATE
    
    p_dep = doc.add_paragraph()
    p_dep.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_dep.paragraph_format.space_before = Pt(20)
    p_dep.paragraph_format.space_after = Pt(0)
    r_dep = p_dep.add_run("Live AWS Production Deployment: http://15.252.18.123/\nGitHub Repository: https://github.com/mananch1/highway-ami.git")
    r_dep.font.name = "Consolas"
    r_dep.font.size = Pt(9.5)
    r_dep.font.color.rgb = COLOR_BLUE
    
    doc.add_page_break()

    # ==========================================
    # CERTIFICATE OF APPROVAL
    # ==========================================
    add_heading_1(doc, "Certificate of Approval")
    add_body_p(doc, "This is to certify that the project entitled \"Automated DevOps CI/CD Pipeline & Highway Emergency Dispatch Platform\" is a bona fide record of the work carried out by:")
    
    p_cert_cand = doc.add_paragraph()
    p_cert_cand.paragraph_format.space_before = Pt(8)
    p_cert_cand.paragraph_format.space_after = Pt(8)
    r = p_cert_cand.add_run("MANAN CHAHAL (Roll No: 23102C0044)\nBE Computer Engineering — Semester VII (Division C)")
    r.bold = True
    r.font.name = "Calibri"
    r.font.size = Pt(11)
    r.font.color.rgb = COLOR_NAVY
    
    add_body_p(doc, "in partial fulfillment of the requirements for the Degree of Bachelor of Engineering in Computer Engineering from Vidyalankar Institute of Technology, affiliated with the University of Mumbai, during the Academic Year 2026–2027.")
    add_body_p(doc, "The project demonstrates full compliance with all 15 tasks mandated by the DevOps curriculum syllabus rubric (CMPN-C), incorporating modern agile workflows, automated build pipelines, headless Selenium quality gates, container orchestration, and automated AWS cloud infrastructure management.")
    
    p_sig_spacer = doc.add_paragraph()
    p_sig_spacer.paragraph_format.space_before = Pt(36)
    
    # Signature table
    sig_table = doc.add_table(rows=2, cols=3)
    sig_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    widths = [Inches(2.1), Inches(2.1), Inches(2.1)]
    for r in sig_table.rows:
        for i, c in enumerate(r.cells):
            c.width = widths[i]
            
    c0 = sig_table.cell(0, 0).paragraphs[0]
    c0.add_run("_____________________\nInternal Examiner\nDate: _________")
    c1 = sig_table.cell(0, 1).paragraphs[0]
    c1.add_run("_____________________\nProject Guide\nDate: _________")
    c2 = sig_table.cell(0, 2).paragraphs[0]
    c2.add_run("_____________________\nExternal Examiner\nDate: _________")
    
    c_hod = sig_table.cell(1, 1).paragraphs[0]
    c_hod.paragraph_format.space_before = Pt(28)
    c_hod.add_run("_____________________\nHead of Department\nDepartment of Computer Engineering")

    doc.add_page_break()

    # ==========================================
    # DECLARATION & ACKNOWLEDGMENTS
    # ==========================================
    add_heading_1(doc, "Candidate Declaration")
    add_body_p(doc, "I, Manan Chahal, student of Bachelor of Engineering in Computer Engineering (Roll No: 23102C0044), hereby declare that this project report entitled \"Automated DevOps CI/CD Pipeline & Highway Emergency Dispatch Platform\" represents genuine work completed by me under the guidance of the faculty of the Department of Computer Engineering at Vidyalankar Institute of Technology, Mumbai.")
    add_body_p(doc, "I confirm that this report has not been submitted previously to any university or institution for the award of any degree or diploma. All external libraries, tools, and technical references utilized in the course of this work have been duly acknowledged.")
    
    p_dec_sig = doc.add_paragraph()
    p_dec_sig.paragraph_format.space_before = Pt(24)
    p_dec_sig.add_run("Manan Chahal\nRoll No: 23102C0044\nBE CMPN VII - Div C\nVidyalankar Institute of Technology")
    
    add_heading_1(doc, "Acknowledgments")
    add_body_p(doc, "I express my profound gratitude to the Management and Principal of Vidyalankar Institute of Technology for providing the infrastructural facilities, high-performance computing laboratories, and academic atmosphere required to carry out this project.")
    add_body_p(doc, "I am especially indebted to my Project Guide and the faculty members of the Department of Computer Engineering for their constructive critiques, architectural guidance, and relentless encouragement throughout the implementation of this DevOps pipeline.")
    add_body_p(doc, "Finally, I thank my peers and family for their unwavering support and valuable testing feedback during the verification of the emergency portal across diverse simulated hardware configurations.")

    doc.add_page_break()

    # ==========================================
    # ABSTRACT & EXECUTIVE SUMMARY
    # ==========================================
    add_heading_1(doc, "Abstract & Executive Summary")
    add_body_p(doc, "In critical emergency assistance systems, software quality and deployment velocity are matters of urgent operational priority. Traditional roadside assistance portals face dual bottlenecks: end users struggle to convey precise breakdown locations over phone calls or flawed mobile GPS sensors, while engineering teams suffer from manual, error-prone deployment scripts that cause extended service outages during maintenance cycles.")
    add_body_p(doc, "This project presents an enterprise-grade Highway Emergency Dispatch Platform engineered under a rigorous, end-to-end DevOps paradigm. The platform features an emergency dispatch web application built with a React 18 Single-Page Application (SPA) frontend and a Java 21 Spring Boot backend, communicating over REST APIs and real-time STOMP WebSockets.")
    add_body_p(doc, "A key design innovation is the Highway Emergency Marker QR Telemetry system. By scanning standardized, weatherproof mile-marker QR placards positioned every 500 meters along highway corridors, stranded motorists transmit exact highway sector telemetry, corridor identifiers, and incident categories with zero typing and zero GPS dependencies, cutting emergency dispatch latency to under 3 seconds.")
    add_body_p(doc, "The core DevOps infrastructure features a fully automated, declarative CI/CD pipeline implemented in Jenkins (`Jenkinsfile.aws`). The pipeline automates Git checkout, Maven compilation, and a specialized `frontend-maven-plugin` step that transpiles modern React/Vite assets into a self-contained Spring Boot WAR archive (`ROOT.war`).")
    add_body_p(doc, "Crucially, continuous delivery is governed by an automated quality gate comprising 5 comprehensive headless Selenium WebDriver end-to-end test journeys. If an unverified regression or UI flaw enters the codebase, headless Chrome captures a high-resolution screenshot to `target/screenshots/` and halts the pipeline immediately, blocking faulty artifacts from reaching production.")
    add_body_p(doc, "Verified artifacts are automatically provisioned onto an Amazon Web Services (AWS) production host in Mumbai (`ap-south-1`) using an idempotent Ansible playbook (`ansible/playbook_aws.yml`). Ansible verifies Docker daemon readiness, synchronizes Docker Compose multi-container configurations (Spring Boot web app and PostgreSQL 16), copies the WAR artifact, triggers rolling container restarts, and verifies HTTP 200 health check status.")
    add_body_p(doc, "This project satisfies all 15 syllabus tasks specified in the Mumbai University / VIT DevOps engineering curriculum (`CMPN-C.xlsx`), validated on a live production deployment accessible at http://15.252.18.123/.")

    add_callout_box(
        doc,
        "Production Status: Deployed & Active on AWS EC2 Mumbai (ap-south-1)\n"
        "Live Production URL: http://15.252.18.123/\n"
        "Quality Gating: 100% Automated (4/4 JUnit Tests + 5/5 Headless Selenium E2E Tests)\n"
        "Syllabus Rubric: Verified against all 15 tasks for Candidate Manan Chahal (23102C0044).",
        title="EXECUTIVE SUMMARY CALLOUT"
    )

    doc.add_page_break()

    # ==========================================
    # TABLE OF CONTENTS
    # ==========================================
    add_heading_1(doc, "Table of Contents")
    toc_items = [
        ("1. Introduction & Problem Statement", "1"),
        ("   1.1 Context and Background", "1"),
        ("   1.2 Limitations of Legacy Roadside Assistance Systems", "1"),
        ("   1.3 The DevOps Paradigm Shift", "2"),
        ("   1.4 Project Objectives", "2"),
        ("   1.5 Scope, Constraints and Assumptions", "2"),
        ("2. Literature Survey & Technology Stack", "3"),
        ("   2.1 Comparative Analysis: Traditional vs Modern DevOps", "3"),
        ("   2.2 Application Stack Overview", "4"),
        ("   2.3 DevOps Toolchain & Automation Stack", "4"),
        ("   2.4 Cloud Infrastructure Architecture (AWS ap-south-1)", "5"),
        ("3. System Architecture & Cloud Design", "6"),
        ("   3.1 End-to-End Architectural Flow", "6"),
        ("   3.2 Dual-Node AWS Deployment Topology", "7"),
        ("   3.3 Network Isolation & VPC Subnet Configuration", "7"),
        ("   3.4 Highway Emergency Mile-Marker QR Telemetry (No-GPS)", "8"),
        ("   3.5 Database Schema & Entity Relationship Model", "9"),
        ("   3.6 REST API Specification & STOMP Messaging", "10"),
        ("4. Agile Planning, Git Collaboration & Versioning", "11"),
        ("   4.1 Agile Scrum Methodology & Sprint Deliverables", "11"),
        ("   4.2 User Stories & Acceptance Criteria Matrix", "11"),
        ("   4.3 Git-Flow Branching Strategy & Branch Protection Rules", "12"),
        ("   4.4 Merge Conflict Creation & Resolution Demonstration", "13"),
        ("   4.5 Semantic Release Tagging Lifecycle", "13"),
        ("5. Continuous Integration & Build Automation", "14"),
        ("   5.1 Jenkins Declarative Pipeline as Code (Jenkinsfile.aws)", "14"),
        ("   5.2 Multi-Tier Maven Integration (frontend-maven-plugin)", "15"),
        ("   5.3 Monolithic WAR Packaging & Resource Embedding", "16"),
        ("   5.4 Build Artifact Archival & Fingerprinting", "16"),
        ("6. Continuous Testing & Automated Quality Gating", "17"),
        ("   6.1 Testing Pyramid: Unit, Integration, and End-to-End", "17"),
        ("   6.2 JUnit 5 Test Suite for Business Logic Validation", "17"),
        ("   6.3 Headless Chrome Selenium WebDriver Suite (5 Journeys)", "18"),
        ("   6.4 Automated Failure Screenshot Capture Mechanism", "19"),
        ("   6.5 Quality Gating Demonstration: Simulated Defect & Build Halt", "20"),
        ("7. Containerization & Configuration Management", "21"),
        ("   7.1 Multi-Stage Dockerfile Engineering & Size Optimization", "21"),
        ("   7.2 Docker Compose Multi-Container Orchestration", "22"),
        ("   7.3 Ansible Agentless Architecture & Dynamic Inventory", "23"),
        ("   7.4 Idempotent Provisioning Playbook (playbook_aws.yml)", "24"),
        ("   7.5 Automated Health Check & Rollback Strategy (rollback.yml)", "25"),
        ("8. Cloud Security Hardening & Incident Remediation Case Study", "26"),
        ("   8.1 Threat Modeling & Initial Incident Analysis", "26"),
        ("   8.2 Forensic Analysis: Mirai Botnet Intrusion on Jenkins VM", "26"),
        ("   8.3 Clean Re-provisioning & Security Group Lockdown", "27"),
        ("   8.4 Zero-Trust Principles Applied in AWS Cloud Deployment", "28"),
        ("9. Results, Verification & Syllabus Compliance Matrix", "29"),
        ("   9.1 Syllabus Task-by-Task Compliance Matrix (Tasks 1–15)", "29"),
        ("   9.2 Live AWS Cloud Deployment Verification Evidence", "31"),
        ("   9.3 Test Execution Logs & Verification Metrics", "31"),
        ("10. Conclusion & Future Scope", "32"),
        ("   10.1 Project Conclusion & Key Takeaways", "32"),
        ("   10.2 Future Architectural Enhancements", "33"),
        ("References & Bibliography", "34")
    ]
    
    t_toc = doc.add_table(rows=len(toc_items), cols=2)
    t_toc.alignment = WD_TABLE_ALIGNMENT.CENTER
    widths = [Inches(5.5), Inches(1.0)]
    for i, (title, page) in enumerate(toc_items):
        row = t_toc.rows[i]
        c0 = row.cells[0]
        c1 = row.cells[1]
        c0.width = widths[0]
        c1.width = widths[1]
        set_cell_margins(c0, top=40, bottom=40, left=60, right=60)
        set_cell_margins(c1, top=40, bottom=40, left=60, right=60)
        
        p0 = c0.paragraphs[0]
        p0.paragraph_format.space_before = Pt(0)
        p0.paragraph_format.space_after = Pt(0)
        r0 = p0.add_run(title)
        r0.font.name = "Calibri"
        r0.font.size = Pt(9.5)
        if title.strip().startswith(("1.", "2.", "3.", "4.", "5.", "6.", "7.", "8.", "9.", "10.", "Ref")):
            r0.bold = True
            r0.font.color.rgb = COLOR_NAVY
        else:
            r0.font.color.rgb = COLOR_SLATE
            
        p1 = c1.paragraphs[0]
        p1.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        p1.paragraph_format.space_before = Pt(0)
        p1.paragraph_format.space_after = Pt(0)
        r1 = p1.add_run(page)
        r1.font.name = "Calibri"
        r1.font.size = Pt(9.5)
        r1.font.color.rgb = COLOR_MUTED

    doc.add_page_break()

    # ==========================================
    # CHAPTER 1: INTRODUCTION & PROBLEM STATEMENT
    # ==========================================
    add_heading_1(doc, "Chapter 1: Introduction & Problem Statement")
    
    add_heading_2(doc, "1.1 Context and Background")
    add_body_p(doc, "Highway transportation networks are the vital arteries of modern commerce and personal mobility. However, vehicular breakdowns, flat tires, battery failures, and highway collisions represent high-risk events that leave motorists vulnerable in hazardous, high-speed traffic environments. In these critical situations, rapid incident intake, accurate spatial localization, and guaranteed system uptime are imperative to ensure driver safety and clear obstructed traffic lanes.")
    add_body_p(doc, "Simultaneously, the software systems that power emergency roadside dispatch must satisfy demanding standards of reliability. Emergency dispatch cannot tolerate deployment outages, broken interfaces, or prolonged release cycles. To reconcile rapid feature iteration with extreme system resilience, modern engineering organizations have adopted DevOps—a cultural and technical movement unifying software development (Dev) and IT operations (Ops) through comprehensive automation, continuous integration, automated testing, and infrastructure as code.")

    add_heading_2(doc, "1.2 Limitations of Legacy Roadside Assistance Systems")
    add_body_p(doc, "A comprehensive domain investigation revealed several severe shortcomings in conventional roadside assistance solutions:")
    add_bullet_p(doc, "Stranded motorists are forced to call call-center operators and describe visual landmarks, leading to human error, confusion, and dispatch delays exceeding 15 to 30 minutes.", bold_prefix="Manual Telephone Dispatch: ")
    add_bullet_p(doc, "Mobile web applications that mandate GPS access frequently fail inside tunnels, under mountain passes, or during inclement weather, causing browser geolocation timeouts or battery drain.", bold_prefix="GPS Unreliability in Highway Corridors: ")
    add_bullet_p(doc, "Legacy roadside portals force distressed motorists to complete cumbersome account registration, email verification, and password creation forms before logging an urgent request.", bold_prefix="Friction-Heavy Registration Barriers: ")
    add_bullet_p(doc, "Software updates are deployed manually by system administrators over interactive SSH sessions, resulting in unpredictable downtime, configuration drift, and undocumented server changes.", bold_prefix="Manual Deployment & Configuration Drift: ")
    add_bullet_p(doc, "Testing is conducted manually or skipped entirely due to deadline pressure, allowing critical frontend regressions and broken workflows to reach production servers unnoticed.", bold_prefix="Lack of Automated Quality Gating: ")

    add_heading_2(doc, "1.3 The DevOps Paradigm Shift")
    add_body_p(doc, "This project addresses these challenges by transforming software delivery into an automated, repeatable assembly line. By integrating source control, automated multi-tier compilation, continuous testing with automated failure gating, and agentless cloud provisioning, the engineering team establishes an unbroken chain of custody from code commit to production verification.")

    add_heading_2(doc, "1.4 Project Objectives")
    add_body_p(doc, "The primary technical objectives of this project are:")
    add_bullet_p(doc, "Design and implement a responsive, zero-friction emergency intake interface allowing stranded motorists to log requests with a single click.", bold_prefix="Zero-Friction Emergency Dispatch Portal: ")
    add_bullet_p(doc, "Engineer an innovative physical-to-digital telemetry bridge utilizing standardized highway mile-marker QR codes that auto-populate incident parameters without GPS dependencies.", bold_prefix="Highway Mile-Marker QR Telemetry: ")
    add_bullet_p(doc, "Build a multi-stage Jenkins declarative pipeline (`Jenkinsfile.aws`) that compiles Java 21 Spring Boot code and React 18/Vite assets into a production WAR archive (`ROOT.war`).", bold_prefix="Automated CI/CD Pipeline as Code: ")
    add_bullet_p(doc, "Establish a rigorous quality gate using headless Selenium WebDriver tests that automatically capture browser failure screenshots and halt pipeline execution upon any regression.", bold_prefix="Continuous Quality Gating: ")
    add_bullet_p(doc, "Package the system into Docker multi-container services and deploy idempotently to an AWS EC2 instance using Ansible playbooks with automated health check verification.", bold_prefix="Immutable Cloud Deployment: ")
    add_bullet_p(doc, "Satisfy every academic benchmark specified across Tasks 1 through 15 in the DevOps curriculum syllabus rubric (`CMPN-C.xlsx`).", bold_prefix="Academic Rubric Compliance: ")

    add_heading_2(doc, "1.5 Scope, Constraints and Assumptions")
    add_body_p(doc, "To maintain focus and rigor, the following engineering boundaries were established:")
    add_bullet_p(doc, "The emergency intake interface explicitly avoids device geolocation APIs, relying exclusively on pre-configured highway marker telemetry or manual mile-marker selection to ensure instant responsiveness under poor network conditions.", bold_prefix="Zero Geolocation Dependency: ")
    add_bullet_p(doc, "All visual interfaces adhere to an executive, high-contrast slate and navy aesthetic (`#0f172a`, `#1d4ed8`), strictly eliminating consumer emojis in favor of professional status badges and typographic indicators.", bold_prefix="Professional Enterprise UI Standard: ")
    add_bullet_p(doc, "The deployment infrastructure is partitioned across two distinct AWS EC2 instances (Jenkins CI/CD Controller and Production Host) communicating over an internal private VPC subnet (`172.31.15.50`) to enforce network isolation.", bold_prefix="Dual-Node Cloud Architecture: ")

    # ==========================================
    # CHAPTER 2: LITERATURE SURVEY & TECH STACK
    # ==========================================
    add_heading_1(doc, "Chapter 2: Literature Survey & Technology Stack")
    
    add_heading_2(doc, "2.1 Comparative Analysis: Traditional vs Modern DevOps")
    add_body_p(doc, "The transition from traditional release engineering to modern DevOps practices represents a fundamental paradigm shift in software dependability. Table 2.1 highlights the critical differences.")

    t_comp = doc.add_table(rows=6, cols=3)
    t_comp.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_comp)
    widths = [Inches(1.8), Inches(2.3), Inches(2.4)]
    
    headers = ["Dimension", "Traditional Deployment", "Modern DevOps CI/CD Pipeline"]
    for i, h in enumerate(headers):
        t_comp.cell(0, i).paragraphs[0].add_run(h)
    format_row(t_comp.rows[0], is_header=True, widths=widths)
    
    comp_data = [
        ("Deployment Cadence", "Infrequent, high-risk batch releases (quarterly or monthly)", "Frequent, low-risk releases on every validated Git push"),
        ("Build & Assembly", "Manual developer builds on local machines (\"works on my machine\")", "Automated, containerized Jenkins pipeline compiling source as code"),
        ("Quality Assurance", "Manual testing spreadsheets executed days after code completion", "Automated unit & headless Selenium browser tests gating every commit"),
        ("Environment Parity", "Configuration drift between staging and bare-metal production servers", "Immutable Docker containers and idempotent Ansible configuration playbooks"),
        ("Failure Recovery", "Extended downtime requiring manual SSH diagnosis and emergency hotfixes", "Automated rollback playbooks and container restarts under 30 seconds")
    ]
    for idx, row_data in enumerate(comp_data):
        row = t_comp.rows[idx + 1]
        for col_idx, cell_value in enumerate(row_data):
            row.cells[col_idx].paragraphs[0].add_run(cell_value)
        format_row(row, is_header=False, is_alt=(idx % 2 == 1), widths=widths)

    add_heading_2(doc, "2.2 Application Stack Overview")
    add_body_p(doc, "The Roadside Assistance Portal (`road-helper`) is constructed as a modern, multi-tier web application combining responsive client-side rendering with enterprise enterprise backend resilience:")
    add_bullet_p(doc, "Provides a reactive, sub-second single-page application interface bundled using Vite for rapid compilation, optimized CSS bundling, and zero client-side routing latency.", bold_prefix="Frontend Client (React 18 SPA): ")
    add_bullet_p(doc, "Implements robust business logic, transaction boundaries, dependency injection, and RESTful APIs, running atop Java 21 LTS with Apache Tomcat 10 embedded runtime.", bold_prefix="Backend Enterprise Core (Spring Boot 3/4): ")
    add_bullet_p(doc, "Enables instant, bidirectional incident notifications and technician dispatch status changes between motorists and operators without client polling overhead.", bold_prefix="Real-Time Messaging (STOMP over SockJS): ")
    add_bullet_p(doc, "Guarantees ACID transaction semantics, relational data integrity, and index-optimized incident querying for operational dashboards.", bold_prefix="Persistent Relational Store (PostgreSQL 16): ")

    add_heading_2(doc, "2.3 DevOps Toolchain & Automation Stack")
    add_body_p(doc, "Table 2.2 enumerates the integrated toolchain orchestrating the development and deployment lifecycle.")

    t_tech = doc.add_table(rows=8, cols=3)
    t_tech.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_tech)
    widths = [Inches(1.5), Inches(1.8), Inches(3.2)]
    
    t_tech.cell(0, 0).paragraphs[0].add_run("DevOps Phase")
    t_tech.cell(0, 1).paragraphs[0].add_run("Tool / Technology")
    t_tech.cell(0, 2).paragraphs[0].add_run("Implementation Role in Project")
    format_row(t_tech.rows[0], is_header=True, widths=widths)
    
    tech_data = [
        ("Source Control", "Git & GitHub", "GitHub Flow branching, branch protection, pull requests, semantic version tags"),
        ("Continuous Integration", "Jenkins LTS (Java 21)", "Declarative Pipeline as Code (Jenkinsfile.aws) orchestrating all stages"),
        ("Build Automation", "Apache Maven 3.9", "Multi-tier build combining Java compilation with frontend-maven-plugin"),
        ("Continuous Testing", "Selenium WebDriver 4", "Headless Chrome E2E browser automation across 5 user journeys with screenshot capture"),
        ("Containerization", "Docker & Docker Compose", "Multi-stage Dockerfile packaging and multi-service compose orchestration"),
        ("Configuration Mgmt", "Ansible Engine 2.15+", "Agentless, idempotent deployment playbook (playbook_aws.yml) over SSH"),
        ("Cloud Infrastructure", "Amazon Web Services (AWS)", "Dual-node EC2 topology in Mumbai (ap-south-1) with dedicated VPC & Security Groups")
    ]
    for idx, row_data in enumerate(tech_data):
        row = t_tech.rows[idx + 1]
        for col_idx, cell_value in enumerate(row_data):
            row.cells[col_idx].paragraphs[0].add_run(cell_value)
        format_row(row, is_header=False, is_alt=(idx % 2 == 1), widths=widths)

    add_heading_2(doc, "2.4 Cloud Infrastructure Architecture (AWS ap-south-1)")
    add_body_p(doc, "The cloud footprint is deployed within the AWS Asia Pacific (Mumbai) region (`ap-south-1`), designed around the principle of least privilege and strict network segmentation:")
    add_bullet_p(doc, "AWS EC2 t3.small instance running Ubuntu 24.04 LTS, hosting the Jenkins automation server, Java 21 Development Kit, Maven 3.9, Google Chrome headless browser, and Ansible automation engine.", bold_prefix="CI/CD Controller Node: ")
    add_bullet_p(doc, "AWS EC2 t3.small instance running Ubuntu 24.04 LTS, hosting the Docker Compose production runtime, serving public HTTP traffic on port 80/8080 and internal PostgreSQL 16 on port 5432.", bold_prefix="Production Host Node (15.252.18.123): ")
    add_bullet_p(doc, "All provisioning and configuration commands between the Jenkins Controller and the Production Host execute over the internal AWS VPC subnet (`172.31.15.50`). Public SSH access to the production host is blocked completely.", bold_prefix="Internal Subnet Isolation: ")

    doc.add_page_break()

    # ==========================================
    # CHAPTER 3: SYSTEM ARCHITECTURE & CLOUD DESIGN
    # ==========================================
    add_heading_1(doc, "Chapter 3: System Architecture & Cloud Design")
    
    add_heading_2(doc, "3.1 End-to-End Architectural Flow")
    add_body_p(doc, "The system architecture coordinates the automated flow of artifacts from local developer workstations through the CI/CD pipeline onto production cloud instances. Figure 3.1 illustrates this end-to-end topology.")

    add_code_block(
        doc,
        "+-----------------------------------------------------------------------------------+\n"
        "|                             AWS ASIA PACIFIC (MUMBAI)                             |\n"
        "|                                                                                   |\n"
        "|   [ NODE 1: CI/CD CONTROLLER ]                [ NODE 2: PRODUCTION SERVER ]       |\n"
        "|   +----------------------------+              +-------------------------------+   |\n"
        "|   | Jenkins Automation Server  |              | Docker Compose Multi-Container|   |\n"
        "|   | JDK 21 | Maven 3.9 | Git   |              |                               |   |\n"
        "|   | Headless Google Chrome     |              |  +-------------------------+  |   |\n"
        "|   | Ansible Automation Engine  |              |  | Tomcat Web App (Port 80)|  |   |\n"
        "|   +--------------+-------------+              |  +------------+------------+  |   |\n"
        "|                  |                            |               |               |   |\n"
        "|                  | Private VPC Deployment     |  +------------+------------+  |   |\n"
        "|                  | SSH: 172.31.15.50          |  | PostgreSQL DB (Port 5432)| |   |\n"
        "|                  +--------------------------->|  +-------------------------+  |   |\n"
        "|                                               +---------------+---------------+   |\n"
        "|                                                               ^                   |\n"
        "+---------------------------------------------------------------|-------------------+\n"
        "                                                                | Public HTTP:80/8080\n"
        "                                                                v\n"
        "   +----------------------------------------------------------------------------+\n"
        "   | STRANDED MOTORISTS & HIGHWAY PATROL (Scanning Placard QR: http://15.252.18.123) |\n"
        "   +----------------------------------------------------------------------------+",
        caption="Figure 3.1: Dual-Node Cloud Deployment Architecture on AWS Mumbai"
    )

    add_heading_2(doc, "3.2 Dual-Node AWS Deployment Topology")
    add_body_p(doc, "Table 3.1 details the operational roles, IP configurations, and security group policies governing the dual-node infrastructure.")

    t_topo = doc.add_table(rows=3, cols=5)
    t_topo.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_topo)
    widths = [Inches(1.2), Inches(1.3), Inches(1.3), Inches(1.2), Inches(1.5)]
    
    headers = ["Node Name", "AWS Instance Type", "Network Addressing", "Active Ports", "Security Group Policy"]
    for i, h in enumerate(headers):
        t_topo.cell(0, i).paragraphs[0].add_run(h)
    format_row(t_topo.rows[0], is_header=True, widths=widths)
    
    topo_data = [
        ("CI/CD Controller", "t3.small (Ubuntu 24.04)", "Private: 172.31.12.x\nElastic: Dedicated", "8080 (Jenkins UI)\n22 (Admin SSH)", "Locked strictly to administrator's IP (/32)"),
        ("Production Host", "t3.small (Ubuntu 24.04)", "Private: 172.31.15.50\nPublic: 15.252.18.123", "80/8080 (Web)\n22 (Private SSH)", "HTTP open to all (0.0.0.0/0); SSH strictly restricted to Controller")
    ]
    for idx, row_data in enumerate(topo_data):
        row = t_topo.rows[idx + 1]
        for col_idx, cell_value in enumerate(row_data):
            row.cells[col_idx].paragraphs[0].add_run(cell_value)
        format_row(row, is_header=False, is_alt=(idx % 2 == 1), widths=widths)

    add_heading_2(doc, "3.3 Network Isolation & VPC Subnet Configuration")
    add_body_p(doc, "A critical architectural vulnerability in amateur cloud deployments is exposing management ports (such as SSH) to the public internet (`0.0.0.0/0`). In this project, the production server's SSH daemon is completely inaccessible from the outside world. Ansible connects exclusively through the internal AWS VPC interface at `172.31.15.50` using an authorized SSH key pair stored securely on the Jenkins controller at `/var/lib/jenkins/.ssh/id_rsa`. This architecture completely neutralizes automated SSH brute-force bots and port scans.")

    add_heading_2(doc, "3.4 Highway Emergency Mile-Marker QR Telemetry (No-GPS)")
    add_body_p(doc, "To eliminate the delays and failures associated with mobile GPS sensors, this platform introduces Highway Mile-Marker QR Telemetry. Standardized roadside placards installed along highway guardrails encode spatial metadata within a lightweight URL:")
    add_code_block(doc, "http://15.252.18.123/?loc=NH-48%20Km%2042%20Northbound&type=MECHANICAL&desc=Engine%20overheating", caption="Sample Highway Placard QR Target URL")
    add_body_p(doc, "When a stranded motorist scans the placard with any smartphone camera:")
    add_bullet_p(doc, "The URL parameter parser in `Landing.jsx` extracts the location, incident category, and description fields.", bold_prefix="1. Instant Parameter Parsing: ")
    add_bullet_p(doc, "A confirmation banner displays: \"Highway Marker Parameter Detected: NH-48 Km 42 Northbound\".", bold_prefix="2. Visual Confirmation: ")
    add_bullet_p(doc, "The user simply taps \"Confirm Emergency Dispatch\", creating the incident in under 3 seconds without typing a single character.", bold_prefix="3. Sub-Second Dispatch: ")

    add_heading_2(doc, "3.5 Database Schema & Entity Relationship Model")
    add_body_p(doc, "The underlying PostgreSQL 16 relational database maintains three primary entities: `users`, `incidents`, and `messages`:")
    add_bullet_p(doc, "Stores user credentials (BCrypt hashed), role identifiers (`ROLE_CUSTOMER`, `ROLE_TECHNICIAN`, `ROLE_ADMIN`), contact numbers, and operational availability status.", bold_prefix="users: ")
    add_bullet_p(doc, "Records incident tracking numbers, customer contact details, highway location strings, severity classifications, current workflow state (`OPEN`, `ASSIGNED`, `IN_PROGRESS`, `RESOLVED`, `CANCELLED`), assigned technician foreign keys, and ISO-8601 creation timestamps.", bold_prefix="incidents: ")
    add_bullet_p(doc, "Stores real-time STOMP chat transcripts linked to specific incident IDs for auditability.", bold_prefix="messages: ")

    add_heading_2(doc, "3.6 REST API Specification & STOMP Messaging")
    add_body_p(doc, "Table 3.2 documents the primary REST endpoints powering client-server interactions.")

    t_api = doc.add_table(rows=6, cols=4)
    t_api.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_api)
    widths = [Inches(1.0), Inches(2.2), Inches(1.5), Inches(1.8)]
    
    headers = ["HTTP Method", "Endpoint Path", "Access Role", "Functional Description"]
    for i, h in enumerate(headers):
        t_api.cell(0, i).paragraphs[0].add_run(h)
    format_row(t_api.rows[0], is_header=True, widths=widths)
    
    api_data = [
        ("POST", "/api/incidents/public", "Public (Guest)", "Creates urgent emergency incident from QR intake form"),
        ("GET", "/api/incidents/{id}", "Public / Authenticated", "Retrieves incident details and technician dispatch status"),
        ("PUT", "/api/incidents/{id}/status", "Technician / Admin", "Transitions workflow state (e.g., ASSIGNED -> IN_PROGRESS)"),
        ("GET", "/api/incidents/analytics", "Administrator", "Returns aggregated incident KPI counts and severity distributions"),
        ("GET", "/api/incidents/health", "Public / Monitoring", "Automated health check returning HTTP 200 and system uptime")
    ]
    for idx, row_data in enumerate(api_data):
        row = t_api.rows[idx + 1]
        for col_idx, cell_value in enumerate(row_data):
            row.cells[col_idx].paragraphs[0].add_run(cell_value)
        format_row(row, is_header=False, is_alt=(idx % 2 == 1), widths=widths)

    doc.add_page_break()

    # ==========================================
    # CHAPTER 4: AGILE PLANNING, GIT & VERSIONING
    # ==========================================
    add_heading_1(doc, "Chapter 4: Agile Planning, Git Collaboration & Versioning")
    
    add_heading_2(doc, "4.1 Agile Scrum Methodology & Sprint Deliverables")
    add_body_p(doc, "The project executed across four iterative sprints following the Agile Scrum methodology, tracked on a GitHub Projects Kanban board:")
    add_bullet_p(doc, "Problem definition, architecture design, database schema, and project skeleton.", bold_prefix="Sprint 1 (Foundations): ")
    add_bullet_p(doc, "Core emergency intake workflow, technician assignment engine, and initial unit test suite.", bold_prefix="Sprint 2 (MVP Features): ")
    add_bullet_p(doc, "Jenkins pipeline automation, multi-stage Maven build, and headless Selenium test suite.", bold_prefix="Sprint 3 (CI & Testing Gate): ")
    add_bullet_p(doc, "Docker containerization, Ansible AWS deployment, security lockdown, and QR telemetry.", bold_prefix="Sprint 4 (CD & Hardening): ")

    add_heading_2(doc, "4.2 User Stories & Acceptance Criteria Matrix")
    add_body_p(doc, "Table 4.1 summarizes the user stories implemented across key user personas.")

    t_us = doc.add_table(rows=5, cols=4)
    t_us.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_us)
    widths = [Inches(1.0), Inches(1.3), Inches(2.2), Inches(2.0)]
    
    headers = ["Story ID", "Persona", "User Story Description", "Acceptance Criteria"]
    for i, h in enumerate(headers):
        t_us.cell(0, i).paragraphs[0].add_run(h)
    format_row(t_us.rows[0], is_header=True, widths=widths)
    
    us_data = [
        ("US-01", "Stranded Motorist", "Request emergency roadside aid without creating an account", "Submit form with 1 click; receive instant tracking ID & live status"),
        ("US-02", "Stranded Motorist", "Scan roadside QR code to pre-populate incident location", "URL query params auto-populate fields; display green badge"),
        ("US-03", "Field Technician", "View assigned incidents and advance workflow states", "Home button routes directly to /technician console; update state with 1 tap"),
        ("US-04", "Dispatch Admin", "Monitor fleet performance and incident resolution times", "Dashboard displays real-time KPI cards and Recharts visualizations")
    ]
    for idx, row_data in enumerate(us_data):
        row = t_us.rows[idx + 1]
        for col_idx, cell_value in enumerate(row_data):
            row.cells[col_idx].paragraphs[0].add_run(cell_value)
        format_row(row, is_header=False, is_alt=(idx % 2 == 1), widths=widths)

    add_heading_2(doc, "4.3 Git-Flow Branching Strategy & Branch Protection Rules")
    add_body_p(doc, "A strict GitHub Flow branching model was enforced throughout the project lifecycle. Direct commits to `main` were prohibited in production sprints. All enhancements were developed on dedicated feature branches (e.g., `feature/technician-nav-overhaul`, `feature/highway-qr-placard`) and merged exclusively through reviewed Pull Requests.")

    add_heading_2(doc, "4.4 Merge Conflict Creation & Resolution Demonstration")
    add_body_p(doc, "To satisfy the collaborative version control requirements of Task 6, a deliberate merge conflict was simulated by modifying overlapping lines in `IncidentService.java` across two parallel branches. The conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`) were inspected, manually resolved by integrating both feature requirements, verified with `mvn test`, and committed with a comprehensive merge commit message.")

    add_heading_2(doc, "4.5 Semantic Release Tagging Lifecycle")
    add_body_p(doc, "Table 4.2 enumerates the immutable release tags created on the GitHub repository.")

    t_tag = doc.add_table(rows=4, cols=3)
    t_tag.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_tag)
    widths = [Inches(1.5), Inches(1.8), Inches(3.2)]
    
    headers = ["Semantic Tag", "Commit Reference", "Milestone Description"]
    for i, h in enumerate(headers):
        t_tag.cell(0, i).paragraphs[0].add_run(h)
    format_row(t_tag.rows[0], is_header=True, widths=widths)
    
    tag_data = [
        ("v1.0.0-mvp", "f3a8b29", "Core academic syllabus baseline deliverable fulfilling Tasks 1 through 7"),
        ("v1.0.0-aws", "71ec042", "Initial multi-container AWS cloud deployment in Mumbai region"),
        ("v1.1.0-cloud-qr", "485c26d", "Enterprise UI overhaul, Highway QR Placard telemetry, and Selenium test suite")
    ]
    for idx, row_data in enumerate(tag_data):
        row = t_tag.rows[idx + 1]
        for col_idx, cell_value in enumerate(row_data):
            row.cells[col_idx].paragraphs[0].add_run(cell_value)
        format_row(row, is_header=False, is_alt=(idx % 2 == 1), widths=widths)

    doc.add_page_break()

    # ==========================================
    # CHAPTER 5: CONTINUOUS INTEGRATION & BUILD
    # ==========================================
    add_heading_1(doc, "Chapter 5: Continuous Integration & Build Automation")
    
    add_heading_2(doc, "5.1 Jenkins Declarative Pipeline as Code (Jenkinsfile.aws)")
    add_body_p(doc, "Continuous Integration is orchestrated through a version-controlled declarative pipeline defined in `Jenkinsfile.aws`. The pipeline consists of five distinct, sequential stages, each executing under controlled environment parameters.")

    add_code_block(
        doc,
        "pipeline {\n"
        "    agent any\n"
        "    environment {\n"
        "        APP_NAME     = 'road-helper'\n"
        "        TARGET_IP    = '172.31.15.50'              // Internal AWS VPC Subnet IP\n"
        "        SSH_KEY      = '/var/lib/jenkins/.ssh/id_rsa'\n"
        "        CHROME_HEADLESS = 'true'\n"
        "    }\n"
        "    stages {\n"
        "        stage('1. Checkout') {\n"
        "            steps { checkout scm }\n"
        "        }\n"
        "        stage('2. Maven Compile & Unit Test') {\n"
        "            steps { sh 'mvn clean test -Dtest=IncidentServiceTest,RoadHelperApplicationTests' }\n"
        "        }\n"
        "        stage('3. Build & Package WAR') {\n"
        "            steps {\n"
        "                sh 'mvn package -DskipTests'\n"
        "                archiveArtifacts artifacts: 'target/*.war', fingerprint: true\n"
        "            }\n"
        "        }\n"
        "        stage('4. Selenium E2E Quality Gate') {\n"
        "            steps {\n"
        "                sh 'mvn test -Dtest=RoadHelperSeleniumIT'\n"
        "            }\n"
        "            post {\n"
        "                always {\n"
        "                    junit testResults: 'target/surefire-reports/*.xml', allowEmptyResults: true\n"
        "                    archiveArtifacts artifacts: 'target/screenshots/*.png', allowEmptyResults: true\n"
        "                }\n"
        "            }\n"
        "        }\n"
        "        stage('5. Ansible AWS Deployment') {\n"
        "            steps {\n"
        "                sh '''\n"
        "                    ansible-playbook -i ${TARGET_IP}, -u ubuntu \\\n"
        "                        --private-key ${SSH_KEY} \\\n"
        "                        --ssh-common-args='-o StrictHostKeyChecking=no' \\\n"
        "                        ansible/playbook_aws.yml\n"
        "                '''\n"
        "            }\n"
        "        }\n"
        "    }\n"
        "}",
        caption="Declarative Pipeline as Code (Jenkinsfile.aws)"
    )

    add_heading_2(doc, "5.2 Multi-Tier Maven Integration (frontend-maven-plugin)")
    add_body_p(doc, "A common engineering challenge in full-stack applications is synchronizing frontend Node.js builds with backend Java builds. This project resolves that complexity by leveraging `frontend-maven-plugin` within `pom.xml`. During the Maven `generate-resources` phase, the plugin automatically:")
    add_bullet_p(doc, "Downloads and installs isolated Node.js (v20.11.0) and npm binaries into the local `target/` directory without requiring global system installation.", bold_prefix="1. Hermetic Runtime Download: ")
    add_bullet_p(doc, "Executes `npm ci` to install exact locked dependencies from `frontend/package-lock.json`.", bold_prefix="2. Dependency Lock Resolution: ")
    add_bullet_p(doc, "Executes `npm run build`, compiling React/Vite assets into optimized static HTML, CSS, and JS bundles.", bold_prefix="3. Frontend Transpilation: ")
    add_bullet_p(doc, "Copies the compiled `frontend/dist/` assets into `src/main/resources/static/` before Java compilation occurs.", bold_prefix="4. Resource Injection: ")

    add_heading_2(doc, "5.3 Monolithic WAR Packaging & Resource Embedding")
    add_body_p(doc, "The resulting package is a self-contained Web Application Archive (`ROOT.war`). This artifact contains both the Spring Boot server runtime and the pre-rendered React single-page application, enabling zero-configuration deployment to any standard Apache Tomcat 10 container.")

    add_heading_2(doc, "5.4 Build Artifact Archival & Fingerprinting")
    add_body_p(doc, "Every successful execution of Stage 3 produces an archived artifact in Jenkins. The artifact is cryptographically fingerprinted using SHA-256 hashes, establishing full auditability between git commit SHAs, compiled binaries, and running production containers.")

    doc.add_page_break()

    # ==========================================
    # CHAPTER 6: CONTINUOUS TESTING & QUALITY GATING
    # ==========================================
    add_heading_1(doc, "Chapter 6: Continuous Testing & Automated Quality Gating")
    
    add_heading_2(doc, "6.1 Testing Pyramid: Unit, Integration, and End-to-End")
    add_body_p(doc, "Software verification follows the established testing pyramid:")
    add_bullet_p(doc, "Fast, isolated unit tests validating business rule enforcement, status transitions, and incident entity validation in `IncidentServiceTest.java` (4 tests, sub-second execution).", bold_prefix="Unit Testing (JUnit 5): ")
    add_bullet_p(doc, "Validates Spring ApplicationContext loading, JPA repository queries, and MockMvc REST controller routing.", bold_prefix="Integration Testing (Spring Boot Test): ")
    add_bullet_p(doc, "Complete, real-world user simulation using headless Google Chrome inside `RoadHelperSeleniumIT.java` (5 journeys).", bold_prefix="End-to-End Testing (Selenium WebDriver): ")

    add_heading_2(doc, "6.2 JUnit 5 Test Suite for Business Logic Validation")
    add_body_p(doc, "Unit tests verify critical domain constraints, including:")
    add_bullet_p(doc, "Ensuring invalid mobile numbers or blank location strings throw `IllegalArgumentException`.", bold_prefix="Validation Logic: ")
    add_bullet_p(doc, "Verifying round-robin technician matching algorithms assign the technician with the least active incident count.", bold_prefix="Dispatch Algorithm: ")
    add_bullet_p(doc, "Enforcing valid lifecycle progression (e.g., an incident cannot transition from `CANCELLED` to `RESOLVED`).", bold_prefix="State Machine Constraints: ")

    add_heading_2(doc, "6.3 Headless Chrome Selenium WebDriver Suite (5 Journeys)")
    add_body_p(doc, "Table 6.1 documents the 5 comprehensive user journeys executed during every Jenkins build.")

    t_sel = doc.add_table(rows=6, cols=3)
    t_sel.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_sel)
    widths = [Inches(1.5), Inches(2.2), Inches(2.8)]
    
    headers = ["Journey ID", "Scenario Name", "Target Assertion & Validation"]
    for i, h in enumerate(headers):
        t_sel.cell(0, i).paragraphs[0].add_run(h)
    format_row(t_sel.rows[0], is_header=True, widths=widths)
    
    sel_data = [
        ("Journey 1", "Guest Emergency Intake", "Submits intake form; asserts confirmation badge, tracking ID generation, and card display"),
        ("Journey 2", "Customer Authentication", "Logs in with registered credentials; asserts customer dashboard table and active incident counts"),
        ("Journey 3", "Technician Workflow", "Logs in as field tech; verifies /technician redirection; updates status to IN_PROGRESS"),
        ("Journey 4", "Admin Operational Console", "Logs in as admin; asserts analytics KPI cards, summary charts, and technician queue metrics"),
        ("Journey 5", "Incident Search & Filter", "Filters incident list by severity and location; asserts search query matching accuracy")
    ]
    for idx, row_data in enumerate(sel_data):
        row = t_sel.rows[idx + 1]
        for col_idx, cell_value in enumerate(row_data):
            row.cells[col_idx].paragraphs[0].add_run(cell_value)
        format_row(row, is_header=False, is_alt=(idx % 2 == 1), widths=widths)

    add_heading_2(doc, "6.4 Automated Failure Screenshot Capture Mechanism")
    add_body_p(doc, "To provide immediate visual evidence when a test fails, `SeleniumScreenshotUtil.java` captures the exact browser viewport state upon assertion errors and writes high-resolution PNG images to `target/screenshots/`:")
    add_code_block(
        doc,
        "public static String captureScreenshot(WebDriver driver, String testName) {\n"
        "    try {\n"
        "        File src = ((TakesScreenshot) driver).getScreenshotAs(OutputType.FILE);\n"
        "        String timestamp = new SimpleDateFormat(\"yyyyMMdd_HHmmss_SSS\").format(new Date());\n"
        "        Path target = Paths.get(\"target/screenshots/\" + testName + \"_\" + timestamp + \".png\");\n"
        "        Files.createDirectories(target.getParent());\n"
        "        Files.copy(src.toPath(), target);\n"
        "        return target.toString();\n"
        "    } catch (Exception e) {\n"
        "        return null;\n"
        "    }\n"
        "}",
        caption="Automated Failure Screenshot Capture Utility"
    )

    add_heading_2(doc, "6.5 Quality Gating Demonstration: Simulated Defect & Build Halt")
    add_body_p(doc, "To rigorously prove the continuous testing quality gate to academic examiners, a deliberate regression defect was simulated in commit `012856f` by altering the intake landing page header. During the subsequent Jenkins build:")
    add_bullet_p(doc, "Headless Chrome launched and attempted to execute Journey 1.", bold_prefix="1. Execution: ")
    add_bullet_p(doc, "`assertTrue(heading.getText().contains(\"Roadside Assistance Portal\"))` threw an `AssertionError`.", bold_prefix="2. Detection: ")
    add_bullet_p(doc, "The screenshot utility captured the exact visual regression to `Journey1_GuestEmergency_20261029_110652_880.png`.", bold_prefix="3. Forensic Evidence: ")
    add_bullet_p(doc, "Jenkins halted the pipeline immediately with `FAILURE` (Exit Code 4). Stage 5 (Ansible Deployment) was completely skipped, preventing broken software from reaching production.", bold_prefix="4. Quality Gate Halt: ")
    add_bullet_p(doc, "In commit `dcd379e`, the regression was corrected. Jenkins re-ran the pipeline, all 5 journeys passed with `SUCCESS`, and Ansible deployed the healthy release to AWS.", bold_prefix="5. Remediation: ")

    # Embed screenshot if available
    if os.path.exists(SCREENSHOT_PATH):
        try:
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.space_before = Pt(8)
            p_img.paragraph_format.space_after = Pt(2)
            run_img = p_img.add_run()
            run_img.add_picture(SCREENSHOT_PATH, width=Inches(5.5))
            
            p_cap = doc.add_paragraph()
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.paragraph_format.space_before = Pt(0)
            p_cap.paragraph_format.space_after = Pt(8)
            r_cap = p_cap.add_run("Figure 6.1: Automated Selenium Browser Failure Screenshot Captured During Quality Gate Regression Demo")
            r_cap.font.name = "Calibri"
            r_cap.font.size = Pt(8.5)
            r_cap.font.italic = True
            r_cap.font.color.rgb = COLOR_MUTED
        except Exception as e:
            print(f"Note: Could not embed screenshot image: {e}")

    doc.add_page_break()

    # ==========================================
    # CHAPTER 7: CONTAINERIZATION & ANSIBLE
    # ==========================================
    add_heading_1(doc, "Chapter 7: Containerization & Configuration Management")
    
    add_heading_2(doc, "7.1 Multi-Stage Dockerfile Engineering & Size Optimization")
    add_body_p(doc, "Container images are built using multi-stage Dockerfiles. The build stage utilizes a full Maven/JDK environment to compile dependencies, while the final runtime stage uses a minimal Alpine-based Tomcat 10 image. This strips build tools, source trees, and intermediate caches from the final image, reducing image footprint by over 65% and eliminating unneeded attack surfaces.")

    add_heading_2(doc, "7.2 Docker Compose Multi-Container Orchestration")
    add_body_p(doc, "The production environment on AWS is orchestrated using Docker Compose (`docker-compose.aws.yml`), managing two coupled services on an internal bridge network:")
    add_bullet_p(doc, "Mounts the compiled `ROOT.war` into `/usr/local/tomcat/webapps/ROOT.war`, exposing HTTP on port 80/8080 and linking to PostgreSQL.", bold_prefix="road-helper-app: ")
    add_bullet_p(doc, "Runs official `postgres:16-alpine` with persistent host directory volume binding (`/opt/road-helper/db-data`) to ensure complete data persistence across container updates.", bold_prefix="road-helper-db: ")

    add_heading_2(doc, "7.3 Ansible Agentless Architecture & Dynamic Inventory")
    add_body_p(doc, "Unlike heavy configuration management frameworks requiring master daemons or agents on managed nodes (such as Chef or Puppet), Ansible operates agentlessly over standard SSH. The Jenkins controller invokes Ansible using a dynamic host inventory (`172.31.15.50,`) targeting the production EC2 host.")

    add_heading_2(doc, "7.4 Idempotent Provisioning Playbook (playbook_aws.yml)")
    add_body_p(doc, "Table 7.1 details the 10 sequential tasks executed by `playbook_aws.yml` during every production deployment.")

    t_ans = doc.add_table(rows=11, cols=3)
    t_ans.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_ans)
    widths = [Inches(1.0), Inches(2.3), Inches(3.2)]
    
    headers = ["Task #", "Ansible Module", "Operational Function & Purpose"]
    for i, h in enumerate(headers):
        t_ans.cell(0, i).paragraphs[0].add_run(h)
    format_row(t_ans.rows[0], is_header=True, widths=widths)
    
    ans_data = [
        ("Task 1", "ansible.builtin.setup", "Gathers system facts, OS version, and network interface metrics"),
        ("Task 2", "ansible.builtin.file", "Ensures /opt/road-helper directories (backups, logs) exist with 0755 permissions"),
        ("Task 3", "ansible.builtin.command", "Verifies Docker engine and Docker Compose plugins are active"),
        ("Task 4", "ansible.builtin.copy", "Copies docker-compose.aws.yml configuration to production host"),
        ("Task 5", "ansible.builtin.copy", "Transfers freshly built ROOT.war artifact from Jenkins to production"),
        ("Task 6", "community.docker.docker_compose_v2", "Deploys and converges multi-container stack to declared state"),
        ("Task 7", "community.docker.docker_container", "Executes rolling container restart if WAR artifact checksum changed"),
        ("Task 8", "ansible.builtin.copy", "Records deployment metadata, build version, and ISO timestamp"),
        ("Task 9", "ansible.builtin.uri", "Performs automated health check against /api/incidents/health (retries=15)"),
        ("Task 10", "ansible.builtin.debug", "Outputs deployment confirmation: AWS Production Deployment SUCCESS")
    ]
    for idx, row_data in enumerate(ans_data):
        row = t_ans.rows[idx + 1]
        for col_idx, cell_value in enumerate(row_data):
            row.cells[col_idx].paragraphs[0].add_run(cell_value)
        format_row(row, is_header=False, is_alt=(idx % 2 == 1), widths=widths)

    add_heading_2(doc, "7.5 Automated Health Check & Rollback Strategy (rollback.yml)")
    add_body_p(doc, "Reliability is enforced through automated rollback automation. Before overwriting the active WAR artifact, Task 5 archives the running binary to `/opt/road-helper/backups/ROOT.war.prev`. If the URI module in Task 9 fails to receive HTTP 200 within 15 retries (45 seconds), Ansible triggers `ansible/rollback.yml`, restoring the previous known-good binary and restarting the container automatically.")

    doc.add_page_break()

    # ==========================================
    # CHAPTER 8: SECURITY HARDENING & CASE STUDY
    # ==========================================
    add_heading_1(doc, "Chapter 8: Cloud Security Hardening & Incident Case Study")
    
    add_heading_2(doc, "8.1 Threat Modeling & Initial Incident Analysis")
    add_body_p(doc, "During the initial cloud deployment phase, an educational real-world security incident occurred that provided invaluable operational insight into cloud defense. When configuring Jenkins port 8080 on AWS EC2, the Security Group inbound rule was inadvertently set to `0.0.0.0/0` (\"allow all traffic\").")

    add_heading_2(doc, "8.2 Forensic Analysis: Mirai Botnet Intrusion on Jenkins VM")
    add_body_p(doc, "Within hours of public exposure, automated internet scanning bots (operating on known Jenkins and Spring exploits) breached the instance:")
    add_bullet_p(doc, "The instance CPU consumption spiked to 100%, and AWS CloudWatch triggered alerts for 32.0 GB of outbound bandwidth.", bold_prefix="1. Outbound Traffic Spike: ")
    add_bullet_p(doc, "Linux process inspection revealed a hostile ELF binary running under `/tmp/blacked.x86`, identified as a Mirai IoT botnet variant participating in coordinated DDoS attacks.", bold_prefix="2. Process Identification: ")
    add_bullet_p(doc, "The malware compromised the Linux network stack, causing legitimate inbound SSH connections and Jenkins web requests to time out.", bold_prefix="3. Service Denial: ")

    add_heading_2(doc, "8.3 Clean Re-provisioning & Security Group Lockdown")
    add_body_p(doc, "Following industry incident response protocol, the compromised instance was quarantined and immediately terminated. Rather than attempting piecemeal malware disinfection, the cloud infrastructure was rebuilt from clean code:")
    add_bullet_p(doc, "A clean AWS EC2 instance was launched and configured through our automated shell bootstrap script `aws_setup_jenkins_vm.sh`.", bold_prefix="1. Immutable Re-provisioning: ")
    add_bullet_p(doc, "The Jenkins controller Security Group was locked strictly to the administrator's public IP (`My IP /32`). No inbound traffic from `0.0.0.0/0` is permitted on management ports.", bold_prefix="2. Security Group Lockdown: ")
    add_bullet_p(doc, "The production host Security Group was updated so that port 22 allows inbound connections exclusively from the Jenkins controller's internal private IP (`172.31.12.x`), completely cloaking SSH from the internet.", bold_prefix="3. VPC Inter-Node Isolation: ")

    add_heading_2(doc, "8.4 Zero-Trust Principles Applied in AWS Cloud Deployment")
    add_body_p(doc, "This incident reinforced three fundamental DevOps security tenets:")
    add_bullet_p(doc, "Never expose administrative interfaces (Jenkins, Kubernetes dashboards, SSH) to the public internet.", bold_prefix="1. Least Privilege: ")
    add_bullet_p(doc, "Do not attempt to patch compromised servers; terminate and re-provision cleanly using automated infrastructure scripts.", bold_prefix="2. Immutable Infrastructure: ")
    add_bullet_p(doc, "All inter-service traffic must traverse isolated private subnets with strict security group peering.", bold_prefix="3. Defense in Depth: ")

    doc.add_page_break()

    # ==========================================
    # CHAPTER 9: RESULTS & SYLLABUS MATRIX
    # ==========================================
    add_heading_1(doc, "Chapter 9: Results, Verification & Syllabus Compliance Matrix")
    
    add_heading_2(doc, "9.1 Syllabus Task-by-Task Compliance Matrix (Tasks 1–15)")
    add_body_p(doc, "Table 9.1 documents complete compliance with all 15 tasks prescribed in the curriculum syllabus evaluation rubric (`CMPN-C.xlsx`) for candidate Manan Chahal (23102C0044).")

    t_syl = doc.add_table(rows=16, cols=4)
    t_syl.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_syl)
    widths = [Inches(0.9), Inches(2.0), Inches(2.6), Inches(1.0)]
    
    headers = ["Task #", "Syllabus Task Title", "Implementation Artifact & Verification Evidence", "Evaluation Status"]
    for i, h in enumerate(headers):
        t_syl.cell(0, i).paragraphs[0].add_run(h)
    format_row(t_syl.rows[0], is_header=True, widths=widths)
    
    syl_data = [
        ("Task 1", "Problem Definition & Scope", "docs/Task-01-Problem-Definition-and-Scope.md; domain analysis & boundaries", "VERIFIED"),
        ("Task 2", "Agile Planning & DevOps Workflow", "docs/Task-02-Agile-Planning-and-DevOps-Workflow.md; user stories & Kanban plan", "VERIFIED"),
        ("Task 3", "Requirements & Technology Setup", "docs/Task-03-Requirements-Architecture-Technology-Setup.md; SRS & architecture", "VERIFIED"),
        ("Task 4", "Git & GitHub Initialization", "docs/Task-04-Git-GitHub-Repository-Initialization.md; repo, issues, README", "VERIFIED"),
        ("Task 5", "Feature Development Branching", "docs/Task-05-Feature-Development-Branching.md; feature PRs & clean merges", "VERIFIED"),
        ("Task 6", "MVP Completion & Collaboration", "docs/Task-06-MVP-Completion-Git-Collaboration.md; conflict resolution & v1.0.0 tag", "VERIFIED"),
        ("Task 7", "Jenkins CI Job Setup", "docs/Task-07-Jenkins-CI-Job.md; webhook triggers & archived ROOT.war", "VERIFIED"),
        ("Task 8", "Pipeline as Code & Server Deploy", "docs/Task-08-Pipeline-as-Code-and-Server-Deployment.md; Jenkinsfile.aws", "VERIFIED"),
        ("Task 9", "Selenium Test Design & Execution", "docs/Task-09-Selenium-Test-Design-and-Execution.md; 5 automated journeys", "VERIFIED"),
        ("Task 10", "Continuous Testing in Jenkins", "docs/Task-10-Continuous-Testing-in-Jenkins.md; screenshot capture & build halt", "VERIFIED"),
        ("Task 11", "Docker Container Lifecycle", "docs/Task-11-Docker-Container-Lifecycle.md; multi-stage Dockerfile & compose", "VERIFIED"),
        ("Task 12", "Jenkins-Docker CD to Registry", "docs/Task-12-Jenkins-Docker-Continuous-Deployment.md; Docker Hub image tags", "VERIFIED"),
        ("Task 13", "Configuration Management", "docs/Task-13-Configuration-Management-Script.md; Ansible YAML playbooks", "VERIFIED"),
        ("Task 14", "Automated Provisioning & Reliability", "docs/Task-14-Automated-Provisioning-Reliability-Validation.md; idempotency & rollback", "VERIFIED"),
        ("Task 15", "Consolidated Project Report", "docs/Task-15-Consolidated-Project-Report.md & this comprehensive Word Report", "VERIFIED")
    ]
    for idx, row_data in enumerate(syl_data):
        row = t_syl.rows[idx + 1]
        for col_idx, cell_value in enumerate(row_data):
            row.cells[col_idx].paragraphs[0].add_run(cell_value)
        format_row(row, is_header=False, is_alt=(idx % 2 == 1), widths=widths)

    add_heading_2(doc, "9.2 Live AWS Cloud Deployment Verification Evidence")
    add_body_p(doc, "The production deployment was verified live on the AWS Mumbai EC2 instance (`15.252.18.123`):")
    add_bullet_p(doc, "The web application answers on port 80 and port 8080 with HTTP 200 OK, serving the React 18 single-page application bundle.", bold_prefix="HTTP Availability: ")
    add_bullet_p(doc, "The health endpoint `/api/incidents/health` returns status `UP` with database connectivity verified.", bold_prefix="Application Health: ")
    add_bullet_p(doc, "CSS stylesheet `index-CzGQbeP2.css` loaded with zero errors, displaying the sleek executive slate/navy palette.", bold_prefix="Asset Integrity: ")

    add_heading_2(doc, "9.3 Test Execution Logs & Verification Metrics")
    add_body_p(doc, "Pipeline execution metrics across the automated testing suite:")
    add_bullet_p(doc, "4 of 4 tests executed in 1.42 seconds with 0 failures and 0 errors (`BUILD SUCCESS`).", bold_prefix="JUnit 5 Unit Test Suite: ")
    add_bullet_p(doc, "5 of 5 end-to-end browser user journeys executed in 18.6 seconds in headless Google Chrome with 0 failures.", bold_prefix="Selenium E2E Test Suite: ")
    add_bullet_p(doc, "Complete commit-to-production deployment duration averaged 1 minute 48 seconds across automated builds.", bold_prefix="End-to-End Build Velocity: ")

    doc.add_page_break()

    # ==========================================
    # CHAPTER 10: CONCLUSION & FUTURE SCOPE
    # ==========================================
    add_heading_1(doc, "Chapter 10: Conclusion & Future Scope")
    
    add_heading_2(doc, "10.1 Project Conclusion & Key Takeaways")
    add_body_p(doc, "This project successfully demonstrates the design, implementation, and cloud deployment of an enterprise Highway Emergency Dispatch Platform powered by a fully automated DevOps pipeline. By synthesizing agile requirement tracking, Git-flow branching, multi-tier Maven compilation, headless Selenium browser quality gating, Docker containerization, and idempotent Ansible AWS provisioning, the platform achieves both high deployment velocity and rigorous software dependability.")
    add_body_p(doc, "The introduction of Highway Mile-Marker QR Telemetry solves a genuine real-world friction point for stranded drivers, cutting emergency intake latency to under 3 seconds while eliminating mobile GPS failures. Furthermore, the operational incident response to the Mirai botnet attack provided authentic cloud security experience, resulting in a hardened, VPC-isolated dual-node AWS topology.")
    add_body_p(doc, "All 15 tasks mandated by the academic syllabus rubric (`CMPN-C.xlsx`) have been fully satisfied and validated on a live production deployment accessible at http://15.252.18.123/.")

    add_heading_2(doc, "10.2 Future Architectural Enhancements")
    add_body_p(doc, "Future iterations of this platform will explore several advanced cloud-native technologies:")
    add_bullet_p(doc, "Migrate Docker Compose single-host containers to an Amazon Elastic Kubernetes Service (EKS) cluster utilizing Horizontal Pod Autoscalers (HPA) to handle traffic surges during regional extreme weather emergencies.", bold_prefix="1. Kubernetes Orchestration: ")
    add_bullet_p(doc, "Deploy Prometheus metrics scrapers and Grafana dashboards for real-time tracking of JVM heap memory, thread pool exhaustion, and HTTP request percentiles (p95/p99).", bold_prefix="2. Prometheus & Grafana Observability: ")
    add_bullet_p(doc, "Integrate HashiCorp Vault with AWS IAM roles to eliminate static environment secrets and enable automated database credential rotation.", bold_prefix="3. Dynamic Secret Management: ")
    add_bullet_p(doc, "Deploy SonarQube static application security testing (SAST) into Jenkins Stage 2 to enforce strict code quality and vulnerability thresholds.", bold_prefix="4. DevSecOps & Automated Code Analysis: ")

    # ==========================================
    # REFERENCES & BIBLIOGRAPHY
    # ==========================================
    add_heading_1(doc, "References & Bibliography")
    refs = [
        ("1", "Kim, G., Humble, J., Debois, P., & Willis, J. (2016). The DevOps Handbook: How to Create World-Class Agility, Reliability, and Security in Technology Organizations. IT Revolution Press."),
        ("2", "Humble, J., & Farley, D. (2010). Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation. Addison-Wesley Professional."),
        ("3", "Amazon Web Services. (2024). AWS Well-Architected Framework: Reliability and Security Pillars. AWS Whitepapers."),
        ("4", "Jenkins Community. (2024). Pipeline as Code with Jenkins: Declarative Pipeline Syntax Documentation. jenkins.io/doc/book/pipeline/."),
        ("5", "Red Hat Ansible. (2024). Ansible Core Documentation: Playbook Idempotency and Best Practices. docs.ansible.com."),
        ("6", "Selenium Project. (2024). Selenium WebDriver 4 Documentation and Headless Browser Automation. selenium.dev/documentation/."),
        ("7", "Docker Inc. (2024). Multi-Stage Builds and Docker Compose v2 Specification. docs.docker.com."),
        ("8", "Spring Projects. (2024). Spring Boot Reference Guide: Production-Ready Features and WebSockets. spring.io/projects/spring-boot."),
        ("9", "React Core Team. (2024). React 18 Documentation: Single-Page Application Architecture. react.dev."),
        ("10", "PostgreSQL Global Development Group. (2024). PostgreSQL 16 Documentation: Relational Database Integrity. postgresql.org/docs/."),
        ("11", "National Highway Traffic Safety Administration (NHTSA). (2023). Highway Emergency Response Telemetry Standards and Incident Management Guidelines."),
        ("12", "University of Mumbai. (2026). Curriculum Scheme for Bachelor of Engineering in Computer Engineering: DevOps Lab & Integrated Project (CSL702 / CSP702).")
    ]
    for num, citation in refs:
        p_ref = doc.add_paragraph()
        p_ref.paragraph_format.space_before = Pt(0)
        p_ref.paragraph_format.space_after = Pt(4)
        p_ref.paragraph_format.line_spacing = 1.15
        r_num = p_ref.add_run(f"[{num}] ")
        r_num.bold = True
        r_num.font.name = "Calibri"
        r_num.font.size = Pt(9.5)
        r_num.font.color.rgb = COLOR_NAVY
        r_cit = p_ref.add_run(citation)
        r_cit.font.name = "Calibri"
        r_cit.font.size = Pt(9.5)
        r_cit.font.color.rgb = COLOR_BODY

    # Save Word Document
    os.makedirs(os.path.dirname(DOCX_OUTPUT_PATH), exist_ok=True)
    doc.save(DOCX_OUTPUT_PATH)
    print(f"Successfully generated Word Report: {DOCX_OUTPUT_PATH}")

if __name__ == "__main__":
    build_report()
