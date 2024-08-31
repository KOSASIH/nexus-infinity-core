package com.nexusinfinitycore.modules.utils;

import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import java.security.SecureRandom;

public class CryptoUtils {
    /**
     * Generates a secret key using a secure random number generator
     * @return the generated secret key
     */
    public static SecretKey generateSecretKey() {
        KeyGenerator keyGenerator = KeyGenerator.getInstance("AES");
        SecureRandom secureRandom = new SecureRandom();
        keyGenerator.init(256, secureRandom);
        return keyGenerator.generateKey();
    }

    /**
     * Encrypts data using a secure encryption algorithm
     * @param data the data to encrypt
     * @param secretKey the secret key to use for encryption
     * @return the encrypted data
     */
    public static byte[] encrypt(byte[] data, SecretKey secretKey) {
        Cipher cipher = Cipher.getInstance("AES");
        cipher.init(Cipher.ENCRYPT_MODE, secretKey);
        return cipher.doFinal(data);
    }

    /**
     * Decrypts data using a secure decryption algorithm
     * @param encryptedData the encrypted data to decrypt
     * @param secretKey the secret key to use for decryption
     * @return the decrypted data
     */
    public static byte[] decrypt(byte[] encryptedData, SecretKey secretKey) {
        Cipher cipher = Cipher.getInstance("AES");
        cipher.init(Cipher.DECRYPT_MODE, secretKey);
        return cipher.doFinal(encryptedData);
    }
}
