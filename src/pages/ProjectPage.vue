<template>
	<q-page class="row items-start justify-evenly text-white">
		<div class="page-size flex column q-my-lg rounded-24 q-py-lg q-px-xl bg-main-dark">
			<div>
				<q-btn
					rounded
					flat
					to="/"
					class="q-mb-md button-back"
				>
					<q-img
						class="arrow-size"
						:src="ArrowLeft"
					></q-img>
				</q-btn>
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

			<TaskList />
		</div>
	</q-page>
</template>

<script
	setup
	lang="ts"
>
import SearchField from '../components/SearchField.vue'
import FilterField from '../components/FilterField.vue'
import TaskList from '../components/TaskList.vue'
import ProjectStatistic from '../components/ProjectStatistic.vue'
import ArrowLeft from '../assets/images/arrow-left.svg'

</script>
