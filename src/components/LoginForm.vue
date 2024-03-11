<template>
	<div class="flex justify-center">
		<q-form class="loginSize flex column bg-main-dark rounded-24 q-pa-xl q-my-lg">
			<h2 class="text-white text-center text-h3">Вход</h2>
			<q-input
				v-model="textLoginEmail"
				rounded
				autofocus
				outlined
				dark
				label="Почта"
				color="purple-10"
				class="text-h6 q-mt-lg"
				type="email"
				lazy-rules
				:rules="[val => val && val.length > 0 || 'Пожалуйста, введите свою почту!']"
			/>
			<q-input
				v-model="textLoginPassword"
				rounded
				outlined
				dark
				label="Пароль"
				color="purple-10"
				class="text-h6 q-mt-lg "
				type="password"
				lazy-rules
				:rules="[val => val && val.length > 0 || 'Пожалуйста, введите свой пароль!']"
			/>
			<div class="flex row items-center justify-between q-gutter-x-xl q-mt-md">
				<q-checkbox
					dark
					color="purple-10"
					v-model="rememberThePassword"
					class="text-white"
					label="Запомнить пароль"
				/>
				<router-link
					to="/"
					class="text-purple-10 text-bold text-center-sm"
				>Забыли пароль?</router-link>
			</div>
			<q-btn
				rounded
				color="purple-10"
				text-color="white"
				label="Войти"
				class="loginBtnSize q-px-lg q-mt-md q-mx-auto"
			/>
			<q-separator
				class=" q-mt-lg"
				color="purple-10"
			/>
			<span class="text-center text-white q-mt-sm">или</span>
			<q-btn
				rounded
				color="white"
				text-color="purple-10"
				label="Зарегистрироваться"
				class="registrationBtnSize q-px-lg q-mt-sm q-mx-auto"
				@click="authStore.isLoginForm = false"
			/>
			<span class="loginConditionsSize text-center q-mt-md text-white q-mx-auto">При регистрации
				и входе вы соглашаетесь с условиями использования
				<b class="cursor-pointer">TaskManager</b> и <u class="cursor-pointer">политикой
					конфиденциальности</u>.</span>
		</q-form>
	</div>
</template>

<script
	setup
	lang="ts"
>
import { ref } from 'vue'
import { useAuthStore } from 'src/stores/auth'

const authStore = useAuthStore()

// во первых у тебя тайпскрипт для того, что делать статическую типизацию. например:
const rememberThePassword = ref<boolean>(true)
const textLoginEmail = ref<string>('')
const textLoginPassword = ref<string>('')

</script>
