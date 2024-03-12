<template>
	<q-header elevated>
		<q-toolbar class="bg-main-dark q-px-xl q-py-md flex justify-between">
			<router-link
				class="text-h5 text-bold q-mr-sm "
				to="/"
			> TaskManager </router-link>
			<q-btn
				v-if="auth"
				to="/profile"
				color="purple-10"
				text-color="white"
				label="Профиль"
				rounded
				class="q-px-lg"
			/>
			<q-btn
				v-else
				to="/login"
				color="purple-10"
				text-color="white"
				label="Войти"
				rounded
				class="q-px-lg"
			/>

		</q-toolbar>
	</q-header>
</template>

<script
	setup
	lang="ts"
>
const auth = false
</script>