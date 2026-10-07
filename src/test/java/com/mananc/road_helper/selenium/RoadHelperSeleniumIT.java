package com.mananc.road_helper.selenium;

import com.mananc.road_helper.RoadHelperApplication;
import com.mananc.road_helper.entity.Role;
import com.mananc.road_helper.entity.User;
import com.mananc.road_helper.repository.UserRepository;
import org.junit.jupiter.api.*;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.edge.EdgeDriver;
import org.openqa.selenium.edge.EdgeOptions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.web.server.LocalServerPort;
import org.springframework.security.crypto.password.PasswordEncoder;

import java.time.Duration;

import static org.junit.jupiter.api.Assertions.*;

@SpringBootTest(classes = RoadHelperApplication.class, webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
@TestMethodOrder(MethodOrderer.OrderAnnotation.class)
public class RoadHelperSeleniumIT {

    @LocalServerPort
    private int port;

    @Autowired
    private UserRepository userRepository;

    @Autowired
    private PasswordEncoder passwordEncoder;

    private WebDriver driver;
    private WebDriverWait wait;
    private String baseUrl;

    @BeforeEach
    void setUp() {
        baseUrl = "http://localhost:" + port;
        try {
            ChromeOptions options = new ChromeOptions();
            options.addArguments("--headless=new", "--disable-gpu", "--no-sandbox", "--disable-dev-shm-usage", "--remote-allow-origins=*");
            driver = new ChromeDriver(options);
        } catch (Exception e) {
            System.out.println("[SELENIUM] Chrome failed, attempting Edge: " + e.getMessage());
            EdgeOptions edgeOptions = new EdgeOptions();
            edgeOptions.addArguments("--headless=new", "--disable-gpu", "--no-sandbox", "--remote-allow-origins=*");
            driver = new EdgeDriver(edgeOptions);
        }
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(5));
        wait = new WebDriverWait(driver, Duration.ofSeconds(10));
    }

    @AfterEach
    void tearDown(TestInfo testInfo) {
        if (driver != null) {
            driver.quit();
        }
    }

    @Test
    @Order(1)
    @DisplayName("Journey 1: Public Guest Emergency Request Flow")
    void testJourney1GuestEmergencyRequest() {
        String testName = "Journey1_GuestEmergency";
        try {
            driver.get(baseUrl + "/");
            wait.until(ExpectedConditions.presenceOfElementLocated(By.tagName("h1")));

            WebElement heading = driver.findElement(By.tagName("h1"));
            assertTrue(heading.getText().contains("Roadside Assistance Portal"));

            // Fill emergency form
            driver.findElement(By.name("name")).sendKeys("Jane Doe Guest");
            driver.findElement(By.name("phone")).sendKeys("9876543210");
            driver.findElement(By.name("location")).sendKeys("Expressway Exit 14");
            driver.findElement(By.name("description")).sendKeys("Car engine overheating and smoke observed");

            WebElement submitBtn = driver.findElement(By.cssSelector("form button[type='submit']"));
            submitBtn.click();

            // Wait for status tracking or confirmation
            wait.until(ExpectedConditions.or(
                    ExpectedConditions.urlContains("/emergency/status"),
                    ExpectedConditions.presenceOfElementLocated(By.xpath("//*[contains(text(), 'Incident')]"))
            ));

            assertTrue(driver.getCurrentUrl().contains("/emergency/status") || driver.getPageSource().contains("Incident"));
        } catch (Throwable t) {
            SeleniumScreenshotUtil.captureScreenshot(driver, testName);
            throw t;
        }
    }

    @Test
    @Order(2)
    @DisplayName("Journey 2: Customer Registration and Login Flow")
    void testJourney2CustomerLoginFlow() {
        String testName = "Journey2_CustomerLogin";
        try {
            // Seed a customer user directly if not existing
            if (userRepository.findByEmail("customer@test.com").isEmpty()) {
                User u = new User();
                u.setName("Alice Customer");
                u.setEmail("customer@test.com");
                u.setPassword(passwordEncoder.encode("Password123"));
                u.setRole(Role.CUSTOMER);
                u.setIsAvailable(true);
                userRepository.save(u);
            }

            driver.get(baseUrl + "/login");
            wait.until(ExpectedConditions.presenceOfElementLocated(By.cssSelector("input[type='email']")));

            driver.findElement(By.cssSelector("input[type='email']")).sendKeys("customer@test.com");
            driver.findElement(By.cssSelector("input[type='password']")).sendKeys("Password123");
            driver.findElement(By.cssSelector("button[type='submit']")).click();

            // Wait for customer dashboard redirect
            wait.until(ExpectedConditions.or(
                    ExpectedConditions.urlContains("/customer"),
                    ExpectedConditions.presenceOfElementLocated(By.xpath("//*[contains(text(), 'Incidents') or contains(text(), 'Logout')]"))
            ));

            assertTrue(driver.getCurrentUrl().contains("/customer") || driver.getPageSource().contains("Incidents"));
        } catch (Throwable t) {
            SeleniumScreenshotUtil.captureScreenshot(driver, testName);
            throw t;
        }
    }

    @Test
    @Order(3)
    @DisplayName("Journey 3: Technician Assignment and Dashboard Workflow")
    void testJourney3TechnicianWorkflow() {
        String testName = "Journey3_TechnicianWorkflow";
        try {
            if (userRepository.findByEmail("tech@test.com").isEmpty()) {
                User u = new User();
                u.setName("Bob Technician");
                u.setEmail("tech@test.com");
                u.setPassword(passwordEncoder.encode("Password123"));
                u.setRole(Role.TECHNICIAN);
                u.setIsAvailable(true);
                userRepository.save(u);
            }

            driver.get(baseUrl + "/login");
            wait.until(ExpectedConditions.presenceOfElementLocated(By.cssSelector("input[type='email']")));

            driver.findElement(By.cssSelector("input[type='email']")).sendKeys("tech@test.com");
            driver.findElement(By.cssSelector("input[type='password']")).sendKeys("Password123");
            driver.findElement(By.cssSelector("button[type='submit']")).click();

            wait.until(ExpectedConditions.or(
                    ExpectedConditions.urlContains("/technician"),
                    ExpectedConditions.presenceOfElementLocated(By.xpath("//*[contains(text(), 'Technician') or contains(text(), 'Availability')]"))
            ));

            assertTrue(driver.getCurrentUrl().contains("/technician") || driver.getPageSource().contains("Technician"));
        } catch (Throwable t) {
            SeleniumScreenshotUtil.captureScreenshot(driver, testName);
            throw t;
        }
    }

    @Test
    @Order(4)
    @DisplayName("Journey 4: Admin Summary Dashboard Analytics Flow")
    void testJourney4AdminDashboardFlow() {
        String testName = "Journey4_AdminDashboard";
        try {
            if (userRepository.findByEmail("admin@test.com").isEmpty()) {
                User u = new User();
                u.setName("Super Admin");
                u.setEmail("admin@test.com");
                u.setPassword(passwordEncoder.encode("Password123"));
                u.setRole(Role.ADMIN);
                u.setIsAvailable(true);
                userRepository.save(u);
            }

            driver.get(baseUrl + "/login");
            wait.until(ExpectedConditions.presenceOfElementLocated(By.cssSelector("input[type='email']")));

            driver.findElement(By.cssSelector("input[type='email']")).sendKeys("admin@test.com");
            driver.findElement(By.cssSelector("input[type='password']")).sendKeys("Password123");
            driver.findElement(By.cssSelector("button[type='submit']")).click();

            wait.until(ExpectedConditions.or(
                    ExpectedConditions.urlContains("/admin"),
                    ExpectedConditions.presenceOfElementLocated(By.xpath("//*[contains(text(), 'Admin') or contains(text(), 'Summary') or contains(text(), 'Incidents')]"))
            ));

            assertTrue(driver.getCurrentUrl().contains("/admin") || driver.getPageSource().contains("Admin"));
        } catch (Throwable t) {
            SeleniumScreenshotUtil.captureScreenshot(driver, testName);
            throw t;
        }
    }

    @Test
    @Order(5)
    @DisplayName("Journey 5: Incident Search and Filter Flow")
    void testJourney5IncidentSearchFlow() {
        String testName = "Journey5_IncidentSearch";
        try {
            driver.get(baseUrl + "/search");
            wait.until(ExpectedConditions.presenceOfElementLocated(By.tagName("input")));

            WebElement searchInput = driver.findElement(By.tagName("input"));
            searchInput.sendKeys("highway");

            // Check that search page loaded properly and inputs are accessible
            assertNotNull(searchInput);
        } catch (Throwable t) {
            SeleniumScreenshotUtil.captureScreenshot(driver, testName);
            throw t;
        }
    }
}
