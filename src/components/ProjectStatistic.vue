<template>
	<div class="flex row justify-center q-gutter-md q-my-md">
		<q-field
			v-for="item in items"
			:key="item"
			rounded
			outlined
			dark
			:label="item.title"
			stack-label
			color="purple-10"
			class="card-size"
		>
			<template v-slot:control>
				<div
					color="purple-10"
					class="self-center"
					tabindex="0"
				>{{ item.description }}</div>
			</template>
		</q-field>

	</div>
</template>

<script
	setup
	lang="ts"
>
import { ref } from 'vue';
const items = ref([
	{ title: 'Количество человек', description: 200 },
	{ title: 'Стоимость', description: 1200 },
	{ title: 'Прогресс', description: 50 },
	{ title: 'Последнее изменение', description: 'Игорь Николаевич - Frontend' },
	{ title: 'Срок сдачи', description: '25.01.2024' },
	{ title: 'Оценка перспективности', description: 'Не перспективный' },
	{ title: 'Стадия разработки', description: 'Аналитика' },
])
</script>