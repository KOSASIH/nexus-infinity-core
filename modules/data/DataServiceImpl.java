package com.nexusinfinitycore.modules.data;

import com.nexusinfinitycore.utils.UtilsModule;

public class DataServiceImpl implements DataModule {
    private final UtilsModule utilsModule;

    public DataServiceImpl(UtilsModule utilsModule) {
        this.utilsModule = utilsModule;
    }

    @Override
    public String getData() {
        return utilsModule.getFormattedString("Sample data from Nexus Infinity Core");
    }
}
