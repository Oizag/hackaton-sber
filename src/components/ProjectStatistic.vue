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
import { useDataStore } from 'src/stores/data'
import { ref } from 'vue';

const dataStore = useDataStore()

const items = ref([
	{ title: 'Количество человек', description: dataStore[0].amountOfPeople },
	{ title: 'Стоимость', description: dataStore[0].price },
	{ title: 'Прогресс', description: dataStore[0].progress },
	{ title: 'Последнее изменение', description: dataStore[0].lastChange },
	{ title: 'Срок сдачи', description: dataStore[0].dueDate },
	{ title: 'Оценка перспективности', description: dataStore[0].condition },
	{ title: 'Стадия разработки', description: dataStore[0].developmentStage },
])
</script>