package com.unicorn.userui.response;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.reflect.TypeToken;
import com.unicorn.userui.model.Client;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.List;

/**
 * Created by Keuvin on 09/09/2017.
 */

public class ClientsResponse {

    private List<Client> clients;

    public ClientsResponse() {
        this.clients = new ArrayList<Client>();
    }


    public static ClientsResponse parseJSON(String response) {
        Gson gson = new GsonBuilder().create();
        Type listType = new TypeToken<List<Client>>() {}.getType();
        ClientsResponse clientsResponse = gson.fromJson(response, ClientsResponse.class);
        return clientsResponse;
    }

    public List<Client> getClients() {
        return clients;
    }
}
