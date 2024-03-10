<template>
	<div
		v-for="item in items"
		:key="item.id"
		class="project-item-shadow main-background q-pa-lg rounded-24 q-mt-md cursor-pointer"
	>
		<!--  -  -  - {{  }} -->
		<div class="flex column">
			<div class="flex row items-start justify-between no-wrap">
				<h3 class="text-h6 text-bold">{{ item.title }}</h3>
				<q-img
					v-if="item.condition === 'bad'"
					class="dotSize q-ma-sm"
					:src="dotRed"
				/>
				<q-img
					v-else-if="item.condition === 'normal'"
					class="dotSize q-ma-sm"
					:src="dotYellow"
				/>
				<q-img
					v-else-if="item.condition === 'good'"
					class="dotSize q-ma-sm"
					:src="dotGreen"
				/>
			</div>
			<p class="q-mt-sm">{{ item.description }}</p>
			<p class=" text-body1 q-mt-md">{{ item.price }} руб.</p>
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
import dotRed from 'images/dot_red.svg'
import dotYellow from 'images/dot_yellow.svg'
import dotGreen from 'images/dot_green.svg'


const current = ref(1)
// const item = ref(['1', 's'])
const items = ref([
	{ id: 0, title: 'Foo', price: 2, description: 'hahah', condition: 'bad' },
	{ id: 1, title: 'Bar', price: 23, description: 'ha123hah', condition: 'good' },
	{ id: 2, title: 'Bar', price: 23, description: 'ha123hah', condition: 'normal' },
])
// const onMounted = () => {
// 	return alert(items.value.id)
// }
// function getPages() {
// 	if (item.id == 10) {
// 		return console.log('hui')
// 	}
// }

</script>
