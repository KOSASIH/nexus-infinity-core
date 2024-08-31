package com.nexusinfinitycore.modules.core;

import com.nexusinfinitycore.utils.UtilsModule;

public class CoreModule {
    private final UtilsModule utilsModule;

    public CoreModule(UtilsModule utilsModule) {
        this.utilsModule = utilsModule;
    }

    public String getWelcomeMessage() {
        return "Welcome to Nexus Infinity Core!";
    }
}
