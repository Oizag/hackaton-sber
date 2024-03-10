import { RouteRecordRaw } from 'vue-router';

const routes: RouteRecordRaw[] = [
	{
		path: '/',
		component: () => import('layouts/MainLayout.vue'),
		children: [
			{
				path: '',
				name: 'IndexPage',
				component: () => import('pages/IndexPage.vue'),
			},
		],
	},
	{
		path: '/:catchAll(.*)*',
		component: () => import('pages/ErrorNotFound.vue'),
	},
	{
		path: '/login',
		component: () => import('layouts/MainLayout.vue'),
		children: [
			{
				path: '',
				name: 'LoginPage',
				component: () => import('pages/LoginPage.vue'),
			},
		],
	},
];

export default routes;
