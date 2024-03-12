<template>
	<q-page class="row items-start justify-evenly text-white">
		<div class="page-profile-size flex column q-my-lg rounded-24 q-py-lg q-px-xl bg-main-dark">
			<div>
				<q-btn
					rounded
					flat
					to="/"
					class="button-back q-mb-md"
				>
					<q-img
						class="arrow-size"
						:src="ArrowLeft"
					></q-img>
				</q-btn>
			</div>
			<h3 class="text-center">{{ }}</h3>
			<div class="flex column justify-center q-gutter-lg q-my-sm">
				<q-field
					rounded
					outlined
					dark
					label="Почта"
					stack-label
					color="purple-10"
					class="card-profile-size"
				>
					<template v-slot:control>
						<p class="text-h6">{{ }}</p>
					</template>
				</q-field>
				<q-field
					rounded
					outlined
					dark
					label="Статус"
					stack-label
					color="purple-10"
					class="card-profile-size"
				>
					<template v-slot:control>
						<p class="text-h6">{{ }}</p>
					</template>
				</q-field>
				<q-field
					rounded
					outlined
					dark
					label="Должность"
					stack-label
					color="purple-10"
					class="card-profile-size"
				>
					<template v-slot:control>
						<p class="text-h6">{{ }}</p>
					</template>
				</q-field>
				<q-field
					rounded
					outlined
					dark
					label="Загруженность"
					stack-label
					color="purple-10"
					class="card-profile-size"
				>
					<template v-slot:control>
						<p class="text-h6">{{ }}</p>
					</template>
				</q-field>
				<q-field
					rounded
					outlined
					dark
					label="Статус"
					stack-label
					color="purple-10"
					class="card-profile-size"
				>
					<template v-slot:control>
						<p class="text-h6">{{ items?.[0].name }}</p>
					</template>
				</q-field>
				<q-btn
					rounded
					class="bg-red-8"
				>Выйти из профиля</q-btn>
			</div>
		</div>
	</q-page>
</template>

<script
	setup
	lang="ts"
>
import { onMounted, ref } from 'vue'
import ArrowLeft from '../assets/images/arrow-left.svg'
import { useEmployee } from 'composables'
import { Employee } from 'models'


const { getEmployeeList } = useEmployee()
const items = ref<Employee[]>()

onMounted(async () => {
	try {
		const { data } = await getEmployeeList()
		items.value = data
		console.log(data)
	} catch (err) {
		console.log(err)
	}
})
</script>