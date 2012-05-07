/* Copyright (c) 2001 - 2007 TOPP - www.openplans.org. All rights reserved.
 * This code is licensed under the GPL 2.0 license, availible at the root
 * application directory.
 */
package org.geonode.security;

import java.io.IOException;
import javax.servlet.http.HttpServletRequest;
import org.geoserver.security.GeoServerAuthenticationProvider;

import org.springframework.security.core.Authentication;
import org.springframework.security.core.AuthenticationException;
import org.springframework.security.authentication.AuthenticationServiceException;
import org.springframework.security.authentication.AuthenticationProvider;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.util.Assert;

/**
 * An {@link AuthenticationProvider} provider passing the username/password to GeoNode for
 * authentication
 * 
 * @author Andrea Aime - OpenGeo
 * 
 */
public class GeoNodeAuthenticationProvider extends GeoServerAuthenticationProvider {

    private GeoNodeSecurityClient client;

    public GeoNodeAuthenticationProvider(GeoNodeSecurityClient client) {
        this.client = client;
    }

    @Override
    public Authentication authenticate(Authentication authentication, HttpServletRequest request) throws AuthenticationException {
        Assert.isInstanceOf(UsernamePasswordAuthenticationToken.class, authentication,
                "authentication shall be a UsernamePasswordAuthenticationToken");
        UsernamePasswordAuthenticationToken token = (UsernamePasswordAuthenticationToken) authentication;
        String username = token.getName();
        String password = (String) token.getCredentials();

        try {
            return client.authenticateUserPwd(username, password);
        } catch (IOException e) {
            throw new AuthenticationServiceException("Communication with GeoNode failed", e);
        }
    }

    @Override
    public boolean supports(Class<? extends Object> authentication, HttpServletRequest request) {
        return (UsernamePasswordAuthenticationToken.class.isAssignableFrom(authentication));
    }

    /**
     * 
     * @param client
     */
    public void setClient(GeoNodeSecurityClient client) {
        this.client = client;
    }

}
