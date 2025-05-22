import { redirect } from '@sveltejs/kit';

export async function handle({ event, resolve }) {
    // Get the token from cookies
    const token = event.cookies.get('token');
    const username = event.cookies.get('username'); // optional, if you're storing it

    // If token exists, set user in locals
    if (token) {
        event.locals.user = {
            name: username,
            token: token
        };
    }

    // Protect /registration_form route
    if (event.url.pathname.startsWith('/registration_form') && !event.locals.user) {
        throw redirect(303, '/login');
    }

    return resolve(event);
}
