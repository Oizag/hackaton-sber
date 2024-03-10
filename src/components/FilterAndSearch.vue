<template>
	<div class="flex row">
		<q-select
			dark
			outlined
			v-model="model"
			:options="options"
			label="Фильтр"
			color="purple-10"
			style="width: 200px;"
		/>
		<q-input
			dark
			outlined
			v-model="text"
			label="Поиск"
			color="purple-10"
			class="q-ml-md"
		>
			<template v-slot:append>
				<q-icon
					name="search"
					size="28px"
				/>
			</template>
		</q-input>
	</div>
</template>

<script
	setup
	lang="ts"
>
import { ref } from 'vue';

const model = ref(null)
const options = [
	'По наименованию', 'По возрастанию', 'По убыванию'
]
const text = ref('')

</script>
