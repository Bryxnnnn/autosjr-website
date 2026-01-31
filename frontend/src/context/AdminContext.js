import React, { createContext, useContext, useState, useEffect } from 'react';

const AdminContext = createContext();

export const AdminProvider = ({ children }) => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [token, setToken] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Check if token exists in localStorage
    const savedToken = localStorage.getItem('admin_token');
    if (savedToken) {
      setToken(savedToken);
      setIsAuthenticated(true);
    }
    setLoading(false);
  }, []);

  const login = (newToken) => {
    localStorage.setItem('admin_token', newToken);
    setToken(newToken);
    setIsAuthenticated(true);
  };

  const logout = () => {
    localStorage.removeItem('admin_token');
    setToken(null);
    setIsAuthenticated(false);
  };

  return (
    <AdminContext.Provider value={{ isAuthenticated, token, login, logout, loading }}>
      {children}
    </AdminContext.Provider>
  );
};

export const useAdmin = () => {
  const context = useContext(AdminContext);
  if (!context) {
    throw new Error('useAdmin must be used within an AdminProvider');
  }
  return context;
};
