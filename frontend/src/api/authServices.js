import { BASE_API } from "../utils/contants";

//* Authentication

export async function loginService(data) {
    try {
      const url = `${BASE_API}/api/auth/login/`;
      const params = {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      };
      const response = await fetch(url, params);
      if (response.status !== 200) {
        throw new Error(response.error);
      }
      const result = await response.json();
  
      return result;
    } catch (error) {
      throw error;
    }
  }
  export async function logoutService(token) {
    try {
      const url = `${BASE_API}/api/auth/logout/`;
      const params = {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authentication: token,
        },
        body: { token: token },
      };
      const response = await fetch(url, params);
      if (response.status !== 200) {
        throw new Error(response.error);
      }
      const result = await response.json();
  
      return result;
    } catch (error) {
      throw error;
    }
  }
  export async function getTokenService(usuario) {
    try {
      const url =
        `${BASE_API}/api/auth/refresh-token/?` +
        new URLSearchParams({ username: usuario });
      const response = await fetch(url);
      return await response.json();
    } catch (error) {
      throw error;
    }
  }