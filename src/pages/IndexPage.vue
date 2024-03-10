<template>
	<q-page class="row items-start justify-evenly text-white">
		<div class="pageSize flex column q-mt-lg rounded-24 q-py-lg q-px-xl bg-main-dark">
			<div class="flex row justify-between items-center">
				<h2 class="text-h4">Проекты</h2>
				<div class="flex justify-end">
					<ModalWindowJSON />
					<FilterAndSearch />
				</div>
			</div>
			<ProjectPanelVue v-for="" />
			<q-pagination
				class="self-center q-mt-lg"
				v-model="current"
				color="purple-10"
				:max="10"
				:max-pages="6"
				boundary-numbers
			/>
		</div>
	</q-page>
</template>

<script
	setup
	lang="ts"
>
import { ref } from 'vue'
import FilterAndSearch from '../components/FilterAndSearch.vue'
import ProjectPanelVue from '../components/ProjectPanel.vue'
import ModalWindowJSON from '../components/ModalWindowJSON.vue'

const current = ref(1)
</script>
