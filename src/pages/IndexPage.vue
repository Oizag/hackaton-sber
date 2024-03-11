<template>
	<q-page class="row items-start justify-evenly text-white">
		<div class="page-size flex column q-mt-lg rounded-24 q-py-lg q-px-xl bg-main-dark">
			<h2 class="text-h4 text-center q-mt-sm">Проекты</h2>
			<div class="page-buttons-wrap flex row justify-between no-wrap q-gutter-md q-my-sm">
				<ModalUpload />
				<FilterField />
				<SearchField />
			</div>
			<ProjectList />
		</div>
	</q-page>
</template>

<script
	setup
	lang="ts"
>
import SearchField from '../components/SearchField.vue'
import FilterField from '../components/FilterField.vue'
import ProjectList from '../components/ProjectList.vue'
import ModalUpload from '../components/ModalUpload.vue'

</script>
