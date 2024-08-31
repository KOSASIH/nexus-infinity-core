package com.nexusinfinitycore.modules.security;

import com.nexusinfinitycore.utils.UtilsModule;

public class SecurityServiceImpl implements SecurityModule {
    private final UtilsModule utilsModule;

    public SecurityServiceImpl(UtilsModule utilsModule) {
        this.utilsModule = utilsModule;
    }

    @Override
    public String encryptData(String data) {
        return utilsModule.encrypt(data, "secret_key_here");
    }

    @Override
    public String decryptData(String data) {
        return utilsModule.decrypt(data, "secret_key_here");
    }
}
