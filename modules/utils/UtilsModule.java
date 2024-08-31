package com.nexusinfinitycore.modules.utils;

public class UtilsModule {
    public String getFormattedString(String input) {
        return String.format("Formatted string: %s", input);
    }

    public String encrypt(String data, String key) {
        // Implement encryption using AES-256-CBC
        return "Encrypted data";
    }

    public String decrypt(String data, String key) {
        // Implement decryption using AES-256-CBC
        return "Decrypted data";
    }
}
