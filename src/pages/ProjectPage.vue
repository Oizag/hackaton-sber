<template>
	<q-page class="row items-start justify-evenly text-white">
		<div class="page-size flex column q-mt-lg rounded-24 q-py-lg q-px-xl bg-main-dark">
			<div class="flex row items-center justify-between q-mt-sm">
				<q-btn
					rounded
					flat
					class="absolute"
					to="/"
				>
					<q-img
						class="arrow-size"
						:src="ArrowLeft"
					></q-img>
				</q-btn>
				<h3 class="q-mx-auto">{{ dataStore[0].name }}</h3>
			</div>
			<ProjectStatistic />
			<q-separator class="bg-purple-10 q-mt-md"></q-separator>
			<div class="page-buttons-wrap flex row justify-between no-wrap q-gutter-md q-my-sm">
				<q-btn
					label="Cоздать задачу"
					color="purple-10"
					class="page-btn-size"
					rounded
				/>
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
import { ref } from 'vue';
import SearchField from '../components/SearchField.vue'
import FilterField from '../components/FilterField.vue'
import ProjectList from '../components/ProjectList.vue'
import ArrowLeft from '../assets/images/arrow-left.svg'
import ProjectStatistic from '../components/ProjectStatistic.vue'
import { useDataStore } from 'src/stores/data'

const dataStore = useDataStore()

</script>
