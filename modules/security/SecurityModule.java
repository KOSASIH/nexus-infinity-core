package com.nexusinfinitycore.modules.security;

import com.nexusinfinitycore.utils.UtilsModule;

public class SecurityModule {
    private final UtilsModule utilsModule;

    public SecurityModule(UtilsModule utilsModule) {
        this.utilsModule = utilsModule;
    }

    public String encryptData(String data) {
        // Implement encryption using AES-256-CBC
        return utilsModule.encrypt(data, "secret_key_here");
    }

    public String decryptData(String data) {
        // Implement decryption using AES-256-CBC
        return utilsModule.decrypt(data, "secret_key_here");
    }
}
