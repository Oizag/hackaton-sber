<template>
	<q-page class="row items-start justify-evenly">
		<Login v-if="authStore.isLoginForm" />
		<Registration v-else />
	</q-page>
</template>

<script
	setup
	lang="ts"
>
import Login from '../components/LoginFrom.vue'
import Registration from '../components/RegistrationForm.vue'
import { useAuthStore } from 'src/stores/auth'

const authStore = useAuthStore()

</script>
