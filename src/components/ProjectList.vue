<template>
	<router-link
		v-for="item in items"
		:key="item.id"
		to="/project"
		class="project-item-shadow main-background q-px-lg q-py-md rounded-24 q-mt-lg cursor-pointer"
		@click="getObjectProject(item)"
	>
		<div class="flex row items-start justify-between no-wrap">
			<h3 class="text-h6 text-bold">{{ item?.name }} ({{ item?.status.label }})</h3>
			<q-img
				v-if="item?.perspective.label === 'Неперспективный'"
				class="dotSize q-ml-md"
				:src="dotRed"
			/>
			<q-img
				v-else-if="item?.perspective.label === 'Нейтральный'"
				class="dotSize q-ml-md"
				:src="dotYellow"
			/>
			<q-img
				v-else-if="item?.perspective.label === 'Перспективный'"
				class="dotSize q-ml-md"
				:src="dotGreen"
			/>
		</div>
		<p class=" text-body1 q-mt-md">{{ item?.cost }} руб.</p>

	</router-link>
	<q-pagination
		class="self-center q-mt-lg"
		v-model="current"
		color="purple-10"
		:max="1"
		:max-pages="6"
		boundary-numbers
	/>

</template>

<script
	setup
	lang="ts"
>
import { onMounted, ref } from 'vue'
import dotRed from 'images/dot_red.svg'
import dotYellow from 'images/dot_yellow.svg'
import dotGreen from 'images/dot_green.svg'
import { useProjectStore } from 'src/stores/data'
import { useProject } from 'composables'
import { Project } from 'models'

const projectStore = useProjectStore()

function getObjectProject(object) {
	projectStore.projectObject = object
	return
}

const { getProjectList } = useProject()
const items = ref<Project[]>()

onMounted(async () => {
	try {
		const { data } = await getProjectList()
		items.value = data
		console.log(data)
	} catch (err) {
		console.log(err)
	}
})

const current = ref<number>(1)
</script>
