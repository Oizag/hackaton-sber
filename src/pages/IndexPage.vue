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
			<ProjectList />
		</div>
	</q-page>
</template>

<script
	setup
	lang="ts"
>
import FilterAndSearch from '../components/FilterAndSearch.vue'
import ProjectList from '../components/ProjectList.vue'
import ModalWindowJSON from '../components/ModalUpload.vue'

</script>
