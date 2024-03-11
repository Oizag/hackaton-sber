<template>
	<q-select
		dark
		outlined
		rounded
		v-model="model"
		:options="options"
		label="Фильтр"
		color="purple-10"
		class="filter-size"
	/>
</template>

<script
	setup
	lang="ts"
>
import { ref } from 'vue';

const model = ref<string>('')
const options = [
	'По наименованию', 'По возрастанию', 'По убыванию'
]
</script>
