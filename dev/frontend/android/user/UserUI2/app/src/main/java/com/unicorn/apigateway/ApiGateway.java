package com.unicorn.apigateway;

import com.unicorn.userui.model.Client;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by jonathan on 21/10/17.
 */

public class ApiGateway {

    public static Object  call(String function, Object data){
        if (function.equals("getClients")){
            return getClients();
        }
        return null;
    }

    private static List<Client> getClients(){
        Client client1 = new Client("1", "Client 1");
        Client client2 = new Client("2", "Client 2");
        Client client3 = new Client("3", "Client 3");
        Client client4 = new Client("4", "Client 4");

        List<Client> clients = new ArrayList<>();
        clients.add(client1);
        clients.add(client2);
        clients.add(client3);
        clients.add(client4);
        return clients;
    }

}
