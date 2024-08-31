package com.nexusinfinitycore.modules.core;

import com.nexusinfinitycore.utils.UtilsModule;

public class CoreServiceImpl implements CoreModule {
    private final UtilsModule utilsModule;

    public CoreServiceImpl(UtilsModule utilsModule) {
        this.utilsModule = utilsModule;
    }

    @Override
    public String getWelcomeMessage() {
        return utilsModule.getFormattedString("Welcome to Nexus Infinity Core!");
    }
}
