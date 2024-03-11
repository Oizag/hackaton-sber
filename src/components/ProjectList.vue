<template>
	<div
		v-for="item in items"
		:key="item"
		:rows="1"
		hide-no-data
		hide-pagination
		:rows-per-page-options="[10]"
		flat
		class="project-item-shadow main-background q-pa-lg rounded-24 q-mt-lg cursor-pointer"
		@click="console.log(items.length)"
	>
		<router-link
			to="/project"
			class="flex column"
		>
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
		</router-link>

	</div>
	<q-pagination
		v-if="Number(items.length / 10) > 1"
		class="self-center q-mt-lg"
		v-model="current"
		color="purple-10"
		:max="Number(items.length / 10)"
		:max-pages="6"
		boundary-numbers
	/>

</template>

<script
	setup
	lang="ts"
>
import { ref } from 'vue'
import dotRed from 'images/dot_red.svg'
import dotYellow from 'images/dot_yellow.svg'
import dotGreen from 'images/dot_green.svg'

const current = ref<number>(1)
const items = ref([
	{ title: 'Foo', price: 2, description: 'hahah', condition: 'bad' },
	{ title: 'Bar', price: 23, description: 'ha123hah', condition: 'good' },
	{ title: 'Bar', price: 23, description: 'ha123hah', condition: 'normal' },
	{ title: 'Bar', price: 23, description: 'ha123hah', condition: 'normal' },
	{ title: 'Bar', price: 23, description: 'ha123hah', condition: 'normal' },
	{ title: 'Bar', price: 23, description: 'ha123hah', condition: 'normal' },
	{ title: 'Bar', price: 23, description: 'ha123hah', condition: 'normal' },
	{ title: 'Bar', price: 23, description: 'ha123hah', condition: 'normal' },

])
</script>
