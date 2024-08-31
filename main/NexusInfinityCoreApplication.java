package com.nexusinfinitycore.main;

import com.nexusinfinitycore.modules.security.SecurityService;
import com.nexusinfinitycore.modules.security.SecurityServiceImpl;
import com.nexusinfinitycore.modules.utils.StringUtils;
import com.nexusinfinitycore.modules.utils.MathUtils;
import com.nexusinfinitycore.modules.utils.CryptoUtils;

public class NexusInfinityCoreApplication {
    private final SecurityService securityService;

    public NexusInfinityCoreApplication() {
        SecurityRepository securityRepository = new SecurityRepositoryImpl(); // Implement a concrete SecurityRepository
        securityService = new SecurityServiceImpl(securityRepository);
    }

    public static void main(String[] args) {
        NexusInfinityCoreApplication application = new NexusInfinityCoreApplication();

        // Demonstrate advanced security features
        String username = "admin";
        String password = "password";
        if (application.securityService.authenticateUser(username, password).join()) {
            System.out.println("Authenticated successfully!");
            String resource = "admin_dashboard";
            if (application.securityService.authorizeUser(username, resource).join()) {
                System.out.println("Authorized to access " + resource);
            } else {
                System.out.println("Access denied to " + resource);
            }
        } else {
            System.out.println("Authentication failed");
        }

        // Demonstrate advanced string manipulation and encryption/decryption capabilities
        String originalString = "Hello, World!";
        String encryptedString = StringUtils.encryptString(originalString);
        System.out.println("Encrypted string: " + encryptedString);
        String decryptedString = StringUtils.decryptString(encryptedString);
        System.out.println("Decrypted string: " + decryptedString);

        // Demonstrate precise mathematical operations
        BigDecimal operand1 = new BigDecimal("10.5");
        BigDecimal operand2 = new BigDecimal("2.5");
        BigDecimal result = MathUtils.performOperation("add", operand1, operand2);
        System.out.println("Result of addition: " + result);

        // Demonstrate generation of random numbers
        int randomNumber = MathUtils.generateRandomNumber(1, 100);
        System.out.println("Random number: " + randomNumber);

        // Demonstrate advanced cryptographic capabilities
        byte[] data = "Hello, World!".getBytes();
        SecretKey secretKey = CryptoUtils.generateSecretKey();
        byte[] encryptedData = CryptoUtils.encrypt(data, secretKey);
        System.out.println("Encrypted data: " + new String(encryptedData));
        byte[] decryptedData = CryptoUtils.decrypt(encryptedData, secretKey);
        System.out.println("Decrypted data: " + new String(decryptedData));
    }
}
