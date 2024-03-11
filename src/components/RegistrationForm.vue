<template>

	<div class="flex justify-center">
		<q-form class=" loginSize flex column bg-main-dark rounded-24 q-pa-xl q-my-lg">
			<h2 class="text-white text-center text-h3">Регистрация</h2>
			<q-input
				v-model="textRegistrationEmail"
				autofocus
				outlined
				rounded
				dark
				label="Почта"
				color="purple-10"
				class="text-h6 q-mt-lg"
				type="email"
				:rules="[val => val && val.length > 0 || 'Пожалуйста, введите свою почту!']"
			/>
			<q-input
				v-model="textRegistrationPassword"
				outlined
				rounded
				dark
				label="Пароль"
				color="purple-10"
				class="text-h6 q-mt-lg"
				type="password"
				:rules="[val => val && val.length > 0 || 'Пожалуйста, введите свой пароль!']"
			/>
			<q-input
				v-model="textRegistrationPasswordRepeat"
				outlined
				rounded
				dark
				label="Повторите пароль"
				color="purple-10"
				class="text-h6 q-mt-lg"
				type="password"
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
			</div>
			<q-btn
				color="purple-10"
				text-color="white"
				label="Зарегистрироваться"
				rounded
				class="registrationBtnSize q-px-lg q-mt-md q-mx-auto"
			/>
			<q-separator
				class=" q-mt-lg"
				color="purple-10"
			/>
			<span class="text-center text-white q-mt-sm">или</span>
			<q-btn
				color="white"
				text-color="purple-10"
				label="Войти"
				rounded
				class="loginBtnSize q-px-lg q-mt-sm q-mx-auto"
				@click="authStore.isLoginForm = true"
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

const rememberThePassword = ref<boolean>(true)
const textRegistrationEmail = ref<string>('')
const textRegistrationPassword = ref<string>('')
const textRegistrationPasswordRepeat = ref<string>('')



</script>
