<template>
	<div class="project-item-shadow main-background q-pa-lg rounded-24 q-mt-lg cursor-pointer">
		<div class="flex column">
			<div class="flex row items-start justify-between no-wrap">
				<h3 class="text-h6 text-bold">Название </h3>
				<q-img
					class="dotSize q-ma-sm"
					:src="dotGreen"
				/>
			</div>
			<p class="q-mt-sm">Lorem ipsum dolor sit amet consectetur adipisicing elit. Similique harum earum
				perspiciatis
				quasi
				reprehenderit eligendi iusto iste laboriosam iure cumque officia dolore quas eaque nesciunt aspernatur,
				nam magni dolorum itaque.</p>
			<p class=" text-body1 q-mt-md">129 млн. руб.</p>
		</div>
	</div>
	<q-pagination
		class="self-center q-mt-lg"
		v-model="current"
		color="purple-10"
		:max="10"
		:max-pages="6"
		boundary-numbers
	/>
</template>

<script
	setup
	lang="ts"
>
import { ref } from 'vue'
import dotRed from '../assets/images/dot_red.svg'
import dotGreen from '../assets/images/dot_green.svg'
import dotYellow from '../assets/images/dot_yellow.svg'

const current = ref(1)
</script>
