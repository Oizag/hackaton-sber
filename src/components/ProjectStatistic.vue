<template>
	<h3 class="q-mx-auto">{{ projectObject.name }}</h3>
	<div class="flex row justify-center q-gutter-md q-my-md">
		<q-field
			rounded
			outlined
			dark
			label="Количество человек"
			stack-label
			color="purple-10"
			class="card-size"
		>
			<template v-slot:control>
				<div
					color="purple-10"
					class="self-center"
					tabindex="0"
				>{{ projectObject.job }}</div>
			</template>
		</q-field>
		<q-field
			rounded
			outlined
			dark
			label="Стоимость"
			stack-label
			color="purple-10"
			class="card-size"
		>
			<template v-slot:control>
				<div
					color="purple-10"
					class="self-center"
					tabindex="0"
				>{{ projectObject.cost }} руб.</div>
			</template>
		</q-field>
		<q-field
			rounded
			outlined
			dark
			label="Прогресс"
			stack-label
			color="purple-10"
			class="card-size"
		>
			<template v-slot:control>
				<div
					color="purple-10"
					class="self-center"
					tabindex="0"
				>{{ projectObject.progress }} %</div>
			</template>
		</q-field>
		<q-field
			rounded
			outlined
			dark
			label="Последнее изменение"
			stack-label
			color="purple-10"
			class="card-size"
		>
			<template v-slot:control>
				<div
					color="purple-10"
					class="self-center"
					tabindex="0"
				>{{ projectObject.lastModifyUser }}</div>
			</template>
		</q-field>
		<q-field
			rounded
			outlined
			dark
			label="Срок сдачи"
			stack-label
			color="purple-10"
			class="card-size"
		>
			<template v-slot:control>
				<div
					color="purple-10"
					class="self-center"
					tabindex="0"
				>{{ projectObject.lastModifyDate }}</div>
			</template>
		</q-field>
		<q-field
			rounded
			outlined
			dark
			label="Оценка перспективности"
			stack-label
			color="purple-10"
			class="card-size"
		>
			<template v-slot:control>
				<div
					color="purple-10"
					class="self-center"
					tabindex="0"
				>{{ projectObject.perspective.label }}</div>
			</template>
		</q-field>
		<q-field
			rounded
			outlined
			dark
			label="Стадия разработки"
			stack-label
			color="purple-10"
			class="card-size"
		>
			<template v-slot:control>
				<div
					color="purple-10"
					class="self-center"
					tabindex="0"
				>{{ projectObject.status.label }}</div>
			</template>
		</q-field>
	</div>
</template>

<script
	setup
	lang="ts"
>
import { onMounted, ref } from 'vue';
import { useProject } from 'composables'
import { Project } from 'models'
import { useProjectStore } from 'src/stores/data'

// по хорошему ты должен был импортнуть этот компонент в родительский и через дефайн пропс передавать сюда айдишник
// а потом в переменную obj(которая тут объявляется, а не в сторе) принимать данные из апи
// где ретрив я тебе сейчас покажу

const projectStore = useProjectStore()
const projectObject = projectStore.projectObject

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

</script>
