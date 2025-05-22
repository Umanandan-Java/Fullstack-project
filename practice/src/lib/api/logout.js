// src/lib/api/logout.js

export async function logout() {
    const response = await fetch('http://localhost:5000/logout', {
        method: 'POST',
        credentials: 'include'  // This ensures the cookie is sent
    });

    if (response.ok) {
        // Optionally redirect or update auth state
        window.location.href = '/login';  // redirect to login page
    } else {
        console.error('Logout failed');
    }
}
