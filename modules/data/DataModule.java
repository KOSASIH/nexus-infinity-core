package com.nexusinfinitycore.modules.data;

import com.nexusinfinitycore.utils.UtilsModule;

public class DataModule {
    private final UtilsModule utilsModule;

    public DataModule(UtilsModule utilsModule) {
        this.utilsModule = utilsModule;
    }

    public String getData() {
        return "Sample data from Nexus Infinity Core";
    }
}
