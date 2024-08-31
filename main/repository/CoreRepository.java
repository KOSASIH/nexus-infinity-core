package com.nexusinfinitycore.main.repository;

import java.util.List;

public interface CoreRepository {
    List<String> getData();
    void storeData(String data);
    boolean authenticate(String username, String password);
    boolean authorize(String role, String resource);
}
