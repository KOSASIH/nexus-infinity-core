package com.nexusinfinitycore.modules.utils;

import java.util.regex.Pattern;

public class StringUtils {
    /**
     * Checks if a string is null or empty
     * @param str the string to check
     * @return true if the string is null or empty, false otherwise
     */
    public static boolean isEmpty(String str) {
        return str == null || str.trim().isEmpty();
    }

    /**
     * Checks if a string matches a regular expression
     * @param str the string to check
     * @param regex the regular expression to match
     * @return true if the string matches the regular expression, false otherwise
     */
    public static boolean matchesRegex(String str, String regex) {
        return Pattern.compile(regex).matcher(str).matches();
    }

    /**
     * Encrypts a string using a secure encryption algorithm
     * @param str the string to encrypt
     * @return the encrypted string
     */
    public static String encryptString(String str) {
        // Use a secure encryption algorithm, such as AES
        return CryptoUtils.encrypt(str, CryptoUtils.generateSecretKey());
    }

    /**
     * Decrypts a string using a secure decryption algorithm
     * @param encryptedStr the encrypted string to decrypt
     * @return the decrypted string
     */
    public static String decryptString(String encryptedStr) {
        // Use a secure decryption algorithm, such as AES
        return CryptoUtils.decrypt(encryptedStr, CryptoUtils.generateSecretKey());
    }
}
