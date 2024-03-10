<template>
	<q-layout
		view="lHh Lpr lFf"
		class="main-background"
	>
		<q-header elevated>
			<q-toolbar class="bg-main-dark q-px-lg q-py-md">
				<q-toolbar-title> TaskManager </q-toolbar-title>
				<q-btn
					color="purple-10"
					text-color="white"
					label="Войти"
					rounded
					class="q-px-lg"
				/>
			</q-toolbar>
		</q-header>

		<q-page-container>
			<!-- <router-view /> -->
			<div
				v-if="login == true"
				class="flex justify-center"
			>
				<q-form
					class="flex column bg-main-dark rounded-24 q-pa-xl q-my-xl"
					style="max-width: 1000px; width: auto"
				>
					<h2 class="text-white text-center text-h3">Вход</h2>
					<q-input
						v-model="textLoginEmail"
						autofocus
						outlined
						dark
						label="Почта"
						color="purple-10"
						class="text-h6 q-mt-lg"
						type="email"
					/>
					<q-input
						v-model="textLoginPassword"
						outlined
						dark
						label="Пароль"
						color="purple-10"
						class="text-h6 q-mt-lg"
						type="password"
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
							class="text-purple-10 text-bold"
						>Забыли пароль?</router-link>
					</div>
					<q-btn
						color="purple-10"
						text-color="white"
						label="Войти"
						rounded
						class="q-px-lg q-mt-md q-mx-auto"
						style="width: 180px"
					/>
					<q-separator
						class=" q-mt-lg"
						color="purple-10"
					/>
					<span class="text-center text-white q-mt-sm">или</span>
					<q-btn
						color="white"
						text-color="purple-10"
						label="Зарегистрироваться"
						rounded
						class="q-px-lg q-mt-sm q-mx-auto"
						style="width: 280px"
						@click="login = !login"
					/>
					<span
						class="text-center q-mt-md text-white q-mx-auto"
						style="max-width: 420px;"
					>При регистрации и входе вы соглашаетесь с условиями использования
						<b class="cursor-pointer">TaskManager</b> и <u class="cursor-pointer :hover">политикой
							конфиденциальности</u>.</span>
				</q-form>
			</div>
			<div
				v-else
				class="flex justify-center"
			>
				<q-form
					class="flex column bg-main-dark rounded-24 q-pa-xl q-my-xl"
					style="max-width: 1000px; width: auto"
				>
					<h2 class="text-white text-center text-h3">Регистрация</h2>
					<q-input
						v-model="textRegistrationEmail"
						autofocus
						outlined
						dark
						label="Почта"
						color="purple-10"
						class="text-h6 q-mt-lg"
						type="email"
					/>
					<q-input
						v-model="textRegistrationPassword"
						outlined
						dark
						label="Пароль"
						color="purple-10"
						class="text-h6 q-mt-lg"
						type="password"
					/>
					<q-input
						v-model="textRegistrationPasswordRepeat"
						outlined
						dark
						label="Повторите пароль"
						color="purple-10"
						class="text-h6 q-mt-lg"
						type="password"
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
						class="q-px-lg q-mt-md q-mx-auto"
						style="width: 280px"
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
						class="q-px-lg q-mt-sm q-mx-auto"
						style="width: 180px"
						@click="login = !login"
					/>
					<span
						class="text-center q-mt-md text-white q-mx-auto"
						style="max-width: 420px;"
					>При регистрации и входе вы соглашаетесь с условиями использования
						<b>TaskManager</b> и политикой
						конфиденциальности.</span>
				</q-form>
			</div>
		</q-page-container>
	</q-layout>
</template>

<script
	setup
	lang="ts"
>
import { reactive, ref } from 'vue'

const rememberThePassword = ref(true)
const login = ref(true)
const textLoginEmail = ref('')
const textLoginPassword = ref('')
const textRegistrationEmail = ref('')
const textRegistrationPassword = ref('')
const textRegistrationPasswordRepeat = ref('')
</script>
