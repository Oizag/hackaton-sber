<template>
	<q-page class="row items-center justify-evenly text-white">
		<div class="pageSize flex column q-mt-xl0. rounded-24 q-py-lg q-px-xl bg-main-dark">
			<div class="flex row justify-between items-center">
				<h2 class="text-h4">Проекты</h2>
				<FilterAndSearch />
			</div>
			<ProjectPanelVue />
		</div>
	</q-page>
</template>

<script
	setup
	lang="ts"
>
import FilterAndSearch from '../components/FilterAndSearch.vue';
import ProjectPanelVue from '../components/ProjectPanel.vue';
</script>
