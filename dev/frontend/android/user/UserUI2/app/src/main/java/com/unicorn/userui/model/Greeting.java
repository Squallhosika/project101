package com.unicorn.userui.model;

import java.io.Serializable;

/**
 * Created by Keuvin on 03/09/2017.
 */

public class Greeting implements Serializable{

    private String id;
    private String content;

    public String getId() {
        return this.id;
    }

    public String getContent() {
        return this.content;
    }

}
