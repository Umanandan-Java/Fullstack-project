import {writable} from 'svelte/store';

export const isAuthenicated = writable(false);
export const role_name = writable('');