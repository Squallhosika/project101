package com.unicorn.userui.model;

import java.io.Serializable;

/**
 * Created by Keuvin on 09/09/2017.
 */

public class Client implements Serializable {

    private String id;
    private String name;

    public String getId() {
        return this.id;
    }

    public String getName() {
        return this.name;
    }
}
