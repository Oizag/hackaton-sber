<template>
	<q-layout
		view="lHh Lpr lFf"
		class="main-background"
	>
		<Header />
		<q-page-container class="q-ma-lg">
			<router-view />
		</q-page-container>
		<Footer />
	</q-layout>
</template>


<script
	setup
	lang="ts"
>

import Header from '../components/HeaderComponent.vue'
import Footer from '../components/FooterComponent.vue'
</script>