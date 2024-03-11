<template>
	<div
		v-for="item in items"
		:key="item.id"
		class="project-item-shadow main-background q-pa-lg rounded-24 q-mt-lg cursor-pointer"
	>
		<router-link
			to="/project"
			class="flex column"
			@click='console.log(items)'
		>
			<div class="flex row items-start justify-between no-wrap">
				<h3 class="text-h6 text-bold">{{ item?.name }}</h3>
				<q-img
					v-if="item?.perspective === 'BAD'"
					class="dotSize q-ma-sm"
					:src="dotRed"
				/>
				<q-img
					v-else-if="item?.perspective === 'NL'"
					class="dotSize q-ma-sm"
					:src="dotYellow"
				/>
				<q-img
					v-else-if="item?.perspective === 'GD'"
					class="dotSize q-ma-sm"
					:src="dotGreen"
				/>
			</div>
			<p class=" text-body1 q-mt-md">{{ item?.cost }} руб.</p>
		</router-link>

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
import dotRed from 'images/dot_red.svg'
import dotYellow from 'images/dot_yellow.svg'
import dotGreen from 'images/dot_green.svg'
import { useProject } from 'composables'
import { Project } from 'models'

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
