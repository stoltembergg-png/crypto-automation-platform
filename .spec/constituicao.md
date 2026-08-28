# Constituição — Plataforma de Automação Cripto

## P-001 [DEVE] Todo requisito declarado pronto tem prova executável

Nenhuma feature é concluída sem `onp-spec verify` e `onp-spec audit --ci` com exit 0.

- verificação(gate): intrínseca ao audit

## P-002 [DEVE] Capital e mainnet permanecem fail-closed sem evidência atual

A matriz canônica deve manter `MAINNET = BLOCKED` nesta fase e toda ativação futura exige prova independente por requisito crítico.

- verificação(teste): @principle:P-002

## P-003 [DEVE] Esta fase não cria runtime financeiro

O repositório de planejamento não pode conter raízes de runtime financeiro (`src/`, `apps/`, `crates/`, `infra/`) nem código de integração, signing, trade ou movimentação de fundos.

- verificação(teste): @principle:P-003

## P-004 [DEVE] Segredos não entram em artefatos de planejamento

Documentação, fila, logs de teste e contratos não podem conter tokens, chaves privadas ou credenciais.

- verificação(teste): @principle:P-004

## P-005 [DEVE] A fila é rastreável e acíclica

Todo cartão da fila possui contrato de pronto e suas dependências não formam ciclo.

- verificação(teste): @principle:P-005
