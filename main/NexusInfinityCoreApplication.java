package com.nexusinfinitycore.main;

import com.nexusinfinitycore.modules.core.CoreModule;
import com.nexusinfinitycore.modules.core.CoreServiceImpl;
import com.nexusinfinitycore.modules.data.DataModule;
import com.nexusinfinitycore.modules.data.DataServiceImpl;
import com.nexusinfinitycore.modules.security.SecurityModule;
import com.nexusinfinitycore.modules.security.SecurityServiceImpl;
import com.nexusinfinitycore.modules.utils.UtilsModule;

public class NexusInfinityCoreApplication {
    public static void main(String[] args) {
        UtilsModule utilsModule = new UtilsModule();
        CoreModule coreModule = new CoreServiceImpl(utilsModule);
        DataModule dataModule = new DataServiceImpl(utilsModule);
        SecurityModule securityModule = new SecurityServiceImpl(utilsModule);

        System.out.println(coreModule.getWelcomeMessage());
        System.out.println(dataModule.getData());

        String encryptedData = securityModule.encryptData("Sample data");
        System.out.println("Encrypted data: " + encryptedData);

        String decryptedData = securityModule.decryptData(encryptedData);
        System.out.println("Decrypted data: " + decryptedData);
    }
}
