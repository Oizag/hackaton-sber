<template>
	<q-input
		dark
		outlined
		rounded
		v-model="search"
		label="Поиск"
		color="purple-10"
		class="search-size"
	>
		<template v-slot:append>
			<q-icon
				name="search"
				size="28px"
			/>
		</template>
	</q-input>
</template>

<script
	setup
	lang="ts"
>
import { ref } from 'vue';

const search = ref<string>('')

</script>
