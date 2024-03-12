<template>
	<div
		v-for="item in items"
		:key="item.id"
	>
		<div
			v-if="item?.project == projectObject.id"
			class="flex row justify-between no-wrap project-item-shadow main-background q-py-md q-px-lg rounded-24 q-mt-lg cursor-pointer"
		>
			<div class="flex column items-start justify-start">
				<h3 class="text-h6 text-bold">{{ item?.title }}</h3>
				<p class=" text-body1 q-mt-sm">{{ item?.descripion }}</p>
			</div>
			<q-img
				v-if="item?.status === 'TD'"
				class="dotSize q-ml-md"
				:src="dotGrey"
			/>
			<q-img
				v-else-if="item?.status === 'IP'"
				class="dotSize q-ml-md"
				:src="dotYellow"
			/>
			<q-img
				v-else-if="item?.status === 'DN'"
				class="dotSize q-ml-md"
				:src="dotGreen"
			/>
		</div>
	</div>
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
import dotGrey from 'images/dot_grey.svg'
import dotYellow from 'images/dot_yellow.svg'
import dotGreen from 'images/dot_green.svg'
import { useTask } from 'composables'
import { Task } from 'models'
import { useProjectStore } from 'src/stores/data'

const projectStore = useProjectStore()
const projectObject = projectStore.projectObject

const { getTaskList } = useTask()
const items = ref<Task[]>()

onMounted(async () => {
	try {
		const { data } = await getTaskList()
		items.value = data
	} catch (err) {
		console.log(err)
	}
})

const current = ref<number>(1)
</script>
