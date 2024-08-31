package com.nexusinfinitycore.main.service;

import java.util.List;

public interface CoreService {
    List<String> getData();
    void storeData(String data);
    boolean authenticate(String username, String password);
    boolean authorize(String role, String resource);
}
