package com.unicorn.userui.model;

import java.io.Serializable;

/**
 * Created by Keuvin on 09/09/2017.
 */

public class Client implements Serializable {

    private String id;
    private String name;

    public Client(String id, String name) {
        this.id = id;
        this.name = name;
    }

    public String getId() {
        return this.id;
    }

    public String getName() {
        return this.name;
    }

    public void setId(String id) {
        this.id = id;
    }

    public void setName(String name) {
        this.name = name;
    }
}
