<template>
	<q-btn
		label="Добавить JSON"
		color="purple-10"
		rounded
		class="page-btn-size"
		@click="modalWindowJSON = true"
	/>
	<q-dialog v-model="modalWindowJSON">
		<q-card
			dark
			class="q-pa-lg flex column align-center"
		>
			<h5>Добавить JSON файл</h5>
			<q-uploader
				dark
				url="http://localhost:4444/upload"
				label="Файл"
				class="uploaderSize rounded-24 q-mt-lg shadow-2"
				color="purple-10"
			/>
			<q-btn
				rounded
				label="Добавить"
				color="purple-10"
				class="q-mt-lg"
				v-close-popup
			/>
		</q-card>
	</q-dialog>
</template>

<script
	setup
	lang="ts"
>
import { ref } from 'vue';

const modalWindowJSON = ref<boolean>(false)
</script>